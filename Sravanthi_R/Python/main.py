# ============================================
# ELECTRICITY USAGE INEQUALITY ANALYSIS
# Complete 4-Step Implementation
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')
import os

# Create directories
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('outputs/figures', exist_ok=True)
os.makedirs('outputs/reports', exist_ok=True)

print("="*70)
print("ELECTRICITY USAGE INEQUALITY ANALYSIS ACROSS CITY ZONES")
print("="*70)

# ============================================
# STEP 1: DATA GENERATION & LOADING
# ============================================
print("\n📊 STEP 1: DATA GENERATION & LOADING")
print("-"*40)

# Generate synthetic electricity consumption data
np.random.seed(42)

# Create timestamps for one year (hourly data)
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='h')

# Define zone characteristics
zones = {
    'Residential': {
        'base_load': 45,
        'peak_hours': [6,7,8,18,19,20,21,22],  # Morning and evening peaks
        'weekend_factor': 1.3,
        'description': 'Houses and apartments'
    },
    'Commercial': {
        'base_load': 75,
        'peak_hours': [9,10,11,12,13,14,15,16,17],  # Business hours
        'weekend_factor': 0.4,
        'description': 'Offices, malls, shops'
    },
    'Industrial': {
        'base_load': 150,
        'peak_hours': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],  # Almost 24/7
        'weekend_factor': 0.8,
        'description': 'Factories, manufacturing'
    },
    'Mixed': {
        'base_load': 60,
        'peak_hours': [7,8,9,10,11,12,13,14,15,16,17,18,19,20],  # Mixed usage
        'weekend_factor': 1.1,
        'description': 'Mixed use areas'
    }
}

# Generate data
data_records = []
for date in dates:
    hour = date.hour
    month = date.month
    is_weekend = 1 if date.weekday() >= 5 else 0
    
    for zone_name, zone_info in zones.items():
        # Base consumption with random variation
        consumption = zone_info['base_load']
        
        # Peak hour multiplier (1.5x to 3x)
        if hour in zone_info['peak_hours']:
            consumption *= np.random.uniform(1.8, 2.5)
        
        # Seasonal effect (summer and winter higher)
        if month in [6,7,8]:  # Summer (AC usage)
            consumption *= np.random.uniform(1.3, 1.6)
        elif month in [12,1,2]:  # Winter (heating)
            consumption *= np.random.uniform(1.2, 1.4)
        
        # Weekend effect
        if is_weekend:
            consumption *= zone_info['weekend_factor']
        
        # Add random noise
        consumption *= np.random.normal(1, 0.15)
        
        # Add some extreme cases for inequality
        if zone_name == 'Industrial' and np.random.random() < 0.1:
            consumption *= 2.0  # occasional high consumption
        if zone_name == 'Residential' and np.random.random() < 0.1:
            consumption *= 0.4  # occasional low consumption
        
        data_records.append({
            'timestamp': date,
            'zone': zone_name,
            'zone_description': zone_info['description'],
            'consumption_kwh': round(max(consumption, 5), 2),  # Min 5 kWh
            'hour': hour,
            'day_of_week': date.dayofweek,
            'month': month,
            'is_weekend': is_weekend,
            'season': 'Summer' if month in [6,7,8] else ('Winter' if month in [12,1,2] else 'Spring/Fall')
        })

# Create DataFrame
df = pd.DataFrame(data_records)

# Save raw data
df.to_csv('data/raw/electricity_consumption_raw.csv', index=False)

print(f"✅ Generated {len(df):,} records")
print(f"✅ Data shape: {df.shape}")
print(f"✅ Zones included: {list(df['zone'].unique())}")
print("\nSample data:")
print(df.head(10))

# ============================================
# STEP 2: FEATURE EXTRACTION
# ============================================
print("\n🔧 STEP 2: FEATURE EXTRACTION")
print("-"*40)

# Extract time-based features
print("Extracting temporal features...")
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
df['day_cycle'] = (df['hour'] + df['day_of_week'] * 24) / 168  # Weekly cycle

# Extract peak indicators
print("Extracting peak indicators...")
df['is_morning_peak'] = df['hour'].isin([6,7,8,9]).astype(int)
df['is_evening_peak'] = df['hour'].isin([17,18,19,20,21,22]).astype(int)
df['is_business_hours'] = df['hour'].isin(range(9,18)).astype(int)

# Extract statistical features per zone
print("Extracting zone statistics...")
zone_stats = df.groupby('zone')['consumption_kwh'].agg(['mean', 'std', 'median']).reset_index()
zone_stats.columns = ['zone', 'zone_mean', 'zone_std', 'zone_median']

# Merge zone statistics back
df = df.merge(zone_stats, on='zone', how='left')

# Calculate deviation features
df['deviation_from_zone_mean'] = df['consumption_kwh'] - df['zone_mean']
df['deviation_from_zone_median'] = df['consumption_kwh'] - df['zone_median']
df['pct_of_zone_mean'] = (df['consumption_kwh'] / df['zone_mean']) * 100
df['z_score'] = (df['consumption_kwh'] - df['zone_mean']) / df['zone_std']

# Extract consumption ratios
print("Extracting consumption ratios...")
daily_avg = df.groupby([df['timestamp'].dt.date, 'zone'])['consumption_kwh'].transform('mean')
df['consumption_vs_daily_avg'] = df['consumption_kwh'] / daily_avg

# Extract inequality indicators
df['is_high_consumption'] = (df['z_score'] > 1.5).astype(int)
df['is_low_consumption'] = (df['z_score'] < -1.5).astype(int)

# Encode categorical features
print("Encoding categorical variables...")
zone_encoder = {zone: i for i, zone in enumerate(df['zone'].unique())}
season_encoder = {season: i for i, season in enumerate(df['season'].unique())}
df['zone_encoded'] = df['zone'].map(zone_encoder)
df['season_encoded'] = df['season'].map(season_encoder)

print(f"✅ Total features extracted: {len(df.columns)}")
print("\nFeature list:")
for i, col in enumerate(df.columns):
    print(f"   {i+1}. {col}")

# Save extracted features
df.to_csv('data/processed/extracted_features.csv', index=False)
print("✅ Features saved to data/processed/extracted_features.csv")

# ============================================
# STEP 3: CLUSTERING ANALYSIS
# ============================================
print("\n🎯 STEP 3: CLUSTERING ANALYSIS")
print("-"*40)

# Prepare features for clustering
print("Preparing features for clustering...")
cluster_features = [
    'consumption_kwh', 'hour', 'is_weekend', 'is_morning_peak', 
    'is_evening_peak', 'deviation_from_zone_mean', 'z_score'
]

# Select and scale features
X_cluster = df[cluster_features].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

# Find optimal number of clusters using elbow method
print("\nFinding optimal number of clusters...")
inertias = []
silhouette_scores = []
K_range = range(2, 9)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.grid(True, alpha=0.3)

# Apply K-Means with optimal k (let's use 4 clusters)
print("Applying K-Means clustering with k=4...")
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Analyze clusters
print("\n📊 Cluster Analysis:")
cluster_summary = df.groupby('cluster').agg({
    'consumption_kwh': ['mean', 'std', 'count'],
    'zone': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'Mixed',
    'is_high_consumption': 'mean',
    'is_low_consumption': 'mean',
    'hour': 'mean'
}).round(2)

print(cluster_summary)

# Visualize clusters with PCA
print("\nVisualizing clusters with PCA...")
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.subplot(2, 3, 2)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('Cluster Visualization (PCA)')

# Cluster characteristics
plt.subplot(2, 3, 3)
cluster_means = df.groupby('cluster')['consumption_kwh'].mean()
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown'][:optimal_k]
plt.bar(range(optimal_k), cluster_means.values, color=colors)
plt.xlabel('Cluster')
plt.ylabel('Average Consumption (kWh)')
plt.title('Average Consumption by Cluster')
for i, v in enumerate(cluster_means.values):
    plt.text(i, v+1, str(round(v,1)), ha='center')

# Zone distribution across clusters
plt.subplot(2, 3, 4)
zone_cluster = pd.crosstab(df['zone'], df['cluster'])
zone_cluster.plot(kind='bar', ax=plt.gca())
plt.title('Zone Distribution Across Clusters')
plt.xlabel('Zone')
plt.ylabel('Count')
plt.legend(title='Cluster')
plt.xticks(rotation=45)

# Consumption patterns by cluster
plt.subplot(2, 3, 5)
for cluster in range(optimal_k):
    cluster_data = df[df['cluster'] == cluster]
    hourly_avg = cluster_data.groupby('hour')['consumption_kwh'].mean()
    plt.plot(hourly_avg.index, hourly_avg.values, marker='o', label=f'Cluster {cluster}')
plt.xlabel('Hour of Day')
plt.ylabel('Average Consumption')
plt.title('Hourly Pattern by Cluster')
plt.legend()
plt.grid(True, alpha=0.3)

# Cluster profiles
plt.subplot(2, 3, 6)
profile_data = df.groupby('cluster')[['is_morning_peak', 'is_evening_peak', 'is_weekend']].mean()
profile_data.plot(kind='bar', ax=plt.gca())
plt.title('Cluster Profiles')
plt.xlabel('Cluster')
plt.ylabel('Proportion')
plt.legend(title='Feature')
plt.xticks(rotation=0)

plt.suptitle('CLUSTERING ANALYSIS RESULTS', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/figures/clustering_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# STEP 4: VISUALIZATION & INTERPRETATION
# ============================================
print("\n📈 STEP 4: VISUALIZATION & INTERPRETATION")
print("-"*40)

# Create comprehensive visualization dashboard
fig = plt.figure(figsize=(20, 16))

# 1. Consumption by Zone - Box Plot
plt.subplot(3, 4, 1)
df.boxplot(column='consumption_kwh', by='zone')
plt.title('Distribution by Zone')
plt.ylabel('Consumption (kWh)')
plt.xticks(rotation=45)

# 2. Average Consumption
plt.subplot(3, 4, 2)
avg_by_zone = df.groupby('zone')['consumption_kwh'].mean().sort_values()
bars = plt.bar(range(len(avg_by_zone)), avg_by_zone.values)
plt.xticks(range(len(avg_by_zone)), avg_by_zone.index, rotation=45)
plt.title('Average Consumption by Zone')
for i, (bar, val) in enumerate(zip(bars, avg_by_zone.values)):
    plt.text(i, val+1, str(round(val,1)), ha='center')

# 3. Total Consumption Share
plt.subplot(3, 4, 3)
total_by_zone = df.groupby('zone')['consumption_kwh'].sum()
plt.pie(total_by_zone.values, labels=total_by_zone.index, autopct='%1.1f%%', 
        startangle=90, colors=sns.color_palette('Set3'))
plt.title('Total Consumption Share')

# 4. Hourly Pattern by Zone
plt.subplot(3, 4, 4)
hourly_zone = df.groupby(['hour', 'zone'])['consumption_kwh'].mean().reset_index()
for zone in df['zone'].unique():
    zone_data = hourly_zone[hourly_zone['zone'] == zone]
    plt.plot(zone_data['hour'], zone_data['consumption_kwh'], marker='.', label=zone, alpha=0.7)
plt.xlabel('Hour')
plt.ylabel('Avg Consumption')
plt.title('Hourly Patterns')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)

# 5. Peak vs Off-peak
plt.subplot(3, 4, 5)
peak_data = df[df['is_evening_peak']==1].groupby('zone')['consumption_kwh'].mean()
offpeak_data = df[df['is_evening_peak']==0].groupby('zone')['consumption_kwh'].mean()
x = range(len(peak_data))
width = 0.35
plt.bar([i - width/2 for i in x], peak_data.values, width, label='Peak Hours', color='orange')
plt.bar([i + width/2 for i in x], offpeak_data.values, width, label='Off-peak', color='lightblue')
plt.xticks(x, peak_data.index, rotation=45)
plt.title('Peak vs Off-peak')
plt.legend()

# 6. Inequality Metrics
plt.subplot(3, 4, 6)
# Calculate Gini-like coefficient (simplified)
def inequality_index(x):
    x = np.array(x)
    if len(x) == 0:
        return 0
    x = x / x.mean()
    return x.std()

inequality = df.groupby('zone')['consumption_kwh'].apply(inequality_index)
colors = ['red' if v > inequality.median() else 'green' for v in inequality]
plt.bar(range(len(inequality)), inequality.values, color=colors)
plt.xticks(range(len(inequality)), inequality.index, rotation=45)
plt.title('Inequality Index (Higher = More Unequal)')
plt.axhline(y=inequality.mean(), color='blue', linestyle='--', alpha=0.5, label='Average')
for i, v in enumerate(inequality.values):
    plt.text(i, v+0.01, f'{v:.3f}', ha='center')

# 7. Weekend vs Weekday
plt.subplot(3, 4, 7)
weekend_data = df[df['is_weekend']==1].groupby('zone')['consumption_kwh'].mean()
weekday_data = df[df['is_weekend']==0].groupby('zone')['consumption_kwh'].mean()
x = range(len(weekend_data))
plt.bar([i - width/2 for i in x], weekend_data.values, width, label='Weekend', color='purple')
plt.bar([i + width/2 for i in x], weekday_data.values, width, label='Weekday', color='pink')
plt.xticks(x, weekend_data.index, rotation=45)
plt.title('Weekend vs Weekday')
plt.legend()

# 8. Seasonal Patterns
plt.subplot(3, 4, 8)
seasonal = df.groupby(['season', 'zone'])['consumption_kwh'].mean().unstack()
seasonal.plot(kind='bar', ax=plt.gca())
plt.title('Seasonal Patterns')
plt.xlabel('Season')
plt.ylabel('Avg Consumption')
plt.xticks(rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 9. High/Low Consumption Zones
plt.subplot(3, 4, 9)
high_low = df.groupby('zone')[['is_high_consumption', 'is_low_consumption']].mean() * 100
high_low.plot(kind='bar', ax=plt.gca(), color=['red', 'green'])
plt.title('High/Low Consumption Events (%)')
plt.xlabel('Zone')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.legend(title='Type')

# 10. Coefficient of Variation
plt.subplot(3, 4, 10)
cv = df.groupby('zone')['consumption_kwh'].apply(lambda x: x.std()/x.mean())
plt.bar(range(len(cv)), cv.values, color='skyblue')
plt.xticks(range(len(cv)), cv.index, rotation=45)
plt.title('Coefficient of Variation')
plt.axhline(y=cv.mean(), color='red', linestyle='--', label=f'Mean: {cv.mean():.3f}')
for i, v in enumerate(cv.values):
    plt.text(i, v+0.01, f'{v:.3f}', ha='center')
plt.legend()

# 11. Cluster Distribution
plt.subplot(3, 4, 11)
cluster_dist = df['cluster'].value_counts().sort_index()
plt.bar(cluster_dist.index, cluster_dist.values, color='orange')
plt.xlabel('Cluster')
plt.ylabel('Count')
plt.title('Cluster Distribution')
for i, v in enumerate(cluster_dist.values):
    plt.text(i, v+100, str(v), ha='center')

# 12. Summary Statistics Table
plt.subplot(3, 4, 12)
plt.axis('off')
summary_text = "SUMMARY STATISTICS\n" + "="*20 + "\n"
summary_text += f"Total Records: {len(df):,}\n"
summary_text += f"Date Range: {df['timestamp'].min()} to {df['timestamp'].max()}\n"
summary_text += f"Overall Avg: {df['consumption_kwh'].mean():.2f} kWh\n"
summary_text += f"Max Consumption: {df['consumption_kwh'].max():.2f} kWh\n"
summary_text += f"Min Consumption: {df['consumption_kwh'].min():.2f} kWh\n"
summary_text += f"Std Deviation: {df['consumption_kwh'].std():.2f}\n"
summary_text += f"Number of Clusters: {optimal_k}\n"
summary_text += f"Most Unequal Zone: {inequality.idxmax()}\n"
summary_text += f"Most Equal Zone: {inequality.idxmin()}\n"
plt.text(0.1, 0.9, summary_text, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('ELECTRICITY USAGE INEQUALITY ANALYSIS - COMPLETE DASHBOARD', 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/figures/complete_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# FINAL REPORT
# ============================================
print("\n📋 GENERATING FINAL REPORT")
print("-"*40)

# Create report
with open('outputs/reports/analysis_report.txt', 'w') as f:
    f.write("="*60 + "\n")
    f.write("ELECTRICITY USAGE INEQUALITY ANALYSIS REPORT\n")
    f.write("="*60 + "\n\n")
    
    f.write("1. DATASET OVERVIEW\n")
    f.write("-"*30 + "\n")
    f.write(f"Total Records: {len(df):,}\n")
    f.write(f"Time Period: {df['timestamp'].min()} to {df['timestamp'].max()}\n")
    f.write(f"Zones Analyzed: {', '.join(df['zone'].unique())}\n\n")
    
    f.write("2. CONSUMPTION STATISTICS BY ZONE\n")
    f.write("-"*30 + "\n")
    for zone in df['zone'].unique():
        zone_data = df[df['zone'] == zone]
        f.write(f"\n{zone} Zone:\n")
        f.write(f"  Average: {zone_data['consumption_kwh'].mean():.2f} kWh\n")
        f.write(f"  Median: {zone_data['consumption_kwh'].median():.2f} kWh\n")
        f.write(f"  Std Dev: {zone_data['consumption_kwh'].std():.2f}\n")
        f.write(f"  Total Share: {(zone_data['consumption_kwh'].sum()/df['consumption_kwh'].sum()*100):.1f}%\n")
    
    f.write("\n3. INEQUALITY METRICS\n")
    f.write("-"*30 + "\n")
    f.write(f"Most Unequal Zone: {inequality.idxmax()} (Index: {inequality.max():.3f})\n")
    f.write(f"Most Equal Zone: {inequality.idxmin()} (Index: {inequality.min():.3f})\n")
    f.write(f"Average Inequality Index: {inequality.mean():.3f}\n\n")
    
    f.write("4. CLUSTERING RESULTS\n")
    f.write("-"*30 + "\n")
    f.write(f"Optimal Clusters: {optimal_k}\n")
    f.write("\nCluster Characteristics:\n")
    for cluster in range(optimal_k):
        cluster_data = df[df['cluster'] == cluster]
        f.write(f"\nCluster {cluster}:\n")
        f.write(f"  Size: {len(cluster_data)} records ({len(cluster_data)/len(df)*100:.1f}%)\n")
        f.write(f"  Avg Consumption: {cluster_data['consumption_kwh'].mean():.2f} kWh\n")
        f.write(f"  Dominant Zone: {cluster_data['zone'].mode()[0]}\n")
    
    f.write("\n5. RECOMMENDATIONS\n")
    f.write("-"*30 + "\n")
    f.write("Based on the analysis, the following recommendations are proposed:\n\n")
    f.write("1. For High Consumption Zones (Industrial/Commercial):\n")
    f.write("   - Implement demand response programs\n")
    f.write("   - Introduce time-of-use pricing\n")
    f.write("   - Energy efficiency audits\n\n")
    f.write("2. For Variable Consumption Zones (Residential):\n")
    f.write("   - Smart meter installation\n")
    f.write("   - Consumer awareness programs\n")
    f.write("   - Peak hour reduction incentives\n\n")
    f.write("3. Infrastructure Improvements:\n")
    f.write("   - Grid modernization\n")
    f.write("   - Energy storage systems\n")
    f.write("   - Renewable energy integration\n")

print("\n✅ ANALYSIS COMPLETE!")
print("="*60)
print("Output files generated:")
print("1. data/raw/electricity_consumption_raw.csv - Raw data")
print("2. data/processed/extracted_features.csv - Features extracted")
print("3. outputs/figures/clustering_analysis.png - Clustering results")
print("4. outputs/figures/complete_dashboard.png - Complete visualization")
print("5. outputs/reports/analysis_report.txt - Final report")
print("="*60)