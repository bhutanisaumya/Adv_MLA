import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    # Scatterplot for points vs games played vs drafted status
    drafted = df[df['drafted'] == 1]
    not_drafted = df[df['drafted'] == 0]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(drafted['GP'], drafted['pts'], label='Drafted', color='blue', marker='o')
    plt.scatter(not_drafted['GP'], not_drafted['pts'], label='Not Drafted', color='red', marker='x')
    
    plt.xlabel('Games Played (GP)')
    plt.ylabel('Points (pts)')
    plt.title('Points vs Games Played vs Drafted Status')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Barplot showing distribution of player heights
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='ht', palette='coolwarm', order=df['ht'].value_counts().index)
    plt.xlabel('Height (ft-inches)')
    plt.ylabel('Count')
    plt.title('Distribution of Player Heights')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Barplot showing number of players in each conference
    blues_palette = sns.color_palette("Blues")
    plt.figure(figsize=(12, 6))
    sns.set_palette(blues_palette)
    sns.countplot(data=df, x='conf', order=df['conf'].value_counts().index)
    plt.xlabel('Conference (conf)')
    plt.ylabel('Count')
    plt.title('Number of Players in Each Conference')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Distribution of points scored
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='pts', bins=20, kde=True)
    plt.xlabel('Points (PTS)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Points Scored')
    plt.grid(axis='y')
    plt.show()
