import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def set_plot_style():
    """Sets a visually appealing style for the plots."""
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titleweight'] = 'bold'

def plot_total_consumption_trend(output_filename="total_consumption_trend.png"):
    """
    Plots the trend of total antibiotic consumption in India.
    Data points are from research indicating consumption in 2010 and 2020.
    """
    print("Generating plot for total antibiotic consumption trend...")
    
    # Data: Year and corresponding consumption in Billion DDDs
    consumption_data = {
        'Year': [2010, 2020],
        'Consumption (Billion DDDs)': [5.411, 7.976]
    }
    df = pd.DataFrame(consumption_data)
    
    plt.figure(figsize=(10, 6))
    lineplot = sns.lineplot(data=df, x='Year', y='Consumption (Billion DDDs)', marker='o', markersize=10, color='#0077b6')
    
    plt.title('Growth of Total Antibiotic Consumption in India (2010-2020)', fontsize=16)
    plt.ylabel('Consumption (Billion DDDs)', fontsize=12)
    plt.xlabel('Year', fontsize=12)
    plt.xticks([2010, 2020])
    plt.ylim(5, 8.5)
    
    # Annotate the data points
    for i in range(df.shape[0]):
        plt.text(df.Year[i], df['Consumption (Billion DDDs)'][i] + 0.1, f"{df['Consumption (Billion DDDs)'][i]}B", 
                 ha='center', fontsize=11, color='#333')

    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    print(f"Saved plot: {output_filename}\n")

def plot_who_aware_comparison(output_filename="who_aware_comparison.png"):
    """
    Plots India's antibiotic consumption mix (Access, Watch, Reserve)
    and compares it with the WHO target.
    """
    print("Generating plot for WHO AWaRe guideline comparison...")

    # Data based on 2019 private-sector consumption
    aware_data = {
        'Category': ['Access', 'Watch', 'Other (Reserve/Unclassified)'],
        'Percentage': [27.0, 54.9, 18.1]
    }
    df = pd.DataFrame(aware_data)
    
    # WHO Target
    who_target_access = 60

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})
    
    # Pie Chart for India's Consumption
    colors = ['#2a9d8f', '#f4a261', '#e76f51']
    explode = (0, 0.05, 0)
    ax1.pie(df['Percentage'], labels=df['Category'], autopct='%1.1f%%',
            startangle=140, colors=colors, explode=explode,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2},
            textprops={'fontsize': 12})
    ax1.set_title("India's Antibiotic Consumption Mix (2019)", fontsize=16, pad=20)
    
    # Bar Chart for WHO Target
    ax2.bar(['WHO Target "Access"'], [who_target_access], color='#2a9d8f', width=0.4)
    ax2.bar(['India "Access"'], [aware_data['Percentage'][0]], color='#a8dadc', width=0.4)
    ax2.set_ylabel('Percentage (%)', fontsize=12)
    ax2.set_ylim(0, 100)
    ax2.set_title('WHO "Access" Group Target', fontsize=16, pad=20)
    ax2.text(0, who_target_access + 2, f'{who_target_access}%', ha='center', color='#333', fontsize=12)
    ax2.text(1, aware_data['Percentage'][0] + 2, f"{aware_data['Percentage'][0]}%", ha='center', color='#333', fontsize=12)
    
    fig.suptitle('India vs. WHO AWaRe Recommendation', fontsize=20, y=1.02)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    print(f"Saved plot: {output_filename}\n")

def plot_top_antibiotic_combinations(output_filename="top_antibiotic_combinations.png"):
    """
    Plots the top-selling fixed-dose antibiotic combinations in India by sales volume.
    Data is from the PMC9511665 study, Table 2.
    """
    print("Generating plot for top antibiotic combinations...")
    
    # Data: Top selling FDCs (Fixed-Dose Combinations) in millions of standard units (2020)
    top_fdcs_data = {
        'Combination': [
            'Amoxicillin + Clavulanic acid',
            'Ampicillin + Cloxacillin',
            'Ofloxacin + Ornidazole',
            'Cefixime + Ofloxacin',
            'Doxycycline + Lactobacillus',
            'Trimethoprim + Sulfamethoxazole',
            'Cefpodoxime + Clavulanic acid'
        ],
        'Sales (Million Units)': [1225.9, 431.4, 314.2, 278.4, 227.0, 214.7, 161.9]
    }
    df = pd.DataFrame(top_fdcs_data)
    
    plt.figure(figsize=(12, 8))
    barplot = sns.barplot(data=df, x='Sales (Million Units)', y='Combination', palette='viridis', orient='h')
    
    plt.title('Top Selling Antibiotic Combinations in India (2020)', fontsize=16)
    plt.xlabel('Sales Volume (Million Standard Units)', fontsize=12)
    plt.ylabel('')
    
    # Add value labels to the bars
    for index, value in enumerate(df['Sales (Million Units)']):
        plt.text(value + 10, index, f'{value:,.1f}', color='black', ha="left", va='center')
        
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    print(f"Saved plot: {output_filename}\n")

def main():
    """
    Main function to run the analysis and generate all plots.
    """
    print("--- Starting Antibiotic Consumption Analysis for India ---")
    
    # --- Summary of Findings ---
    per_capita_consumption = "10.4 DDD/1000 inhabitants/day (2019)"
    total_consumption_2019 = "5.07 Billion DDDs"
    
    print("\nKey Metrics:")
    print(f"  - Per Capita Consumption: {per_capita_consumption}")
    print(f"  - Total Private Sector Consumption (2019): {total_consumption_2019}")
    print("  - WHO Guideline Compliance: Significantly below the 60% 'Access' group target.\n")
    
    # --- Generate Visualizations ---
    set_plot_style()
    plot_total_consumption_trend()
    plot_who_aware_comparison()
    plot_top_antibiotic_combinations()
    
    print("--- Analysis Complete. All plots have been generated. ---")

if __name__ == '__main__':
    main()
