import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Year': [1971, 1974, 1978, 1982, 1989, 1993, 1997, 1999, 2004, 2008, 2012, 2017, 2019, 2020, 2022, 2024],
    'Transistors': [
        2250,           # 1971: Intel 4004
        6000,           # 1974: Intel 8080
        29000,          # 1978: Intel 8086
        134000,         # 1982: Intel 80286
        1180000,        # 1989: Intel 80486
        3100000,        # 1993: Pentium
        7500000,        # 1997: Pentium II
        9500000,        # 1999: Pentium III
        125000000,      # 2004: Pentium 4
        731000000,      # 2008: Core i7
        1400000000,     # 2012: Core i7 (Ivy Bridge)
        4800000000,     # 2017: AMD Ryzen 1000
        9800000000,     # 2019: AMD Ryzen 3000
        11400000000,    # 2020: Apple M1
        20000000000,    # 2022: Apple M2
        28000000000     # 2024: Apple M4
    ]
}

df = pd.DataFrame(data)

# plot
plt.figure(figsize=(10, 6))


plt.scatter(df['Year'], df['Transistors'], color='blue', s=50)


plt.yscale('log')


plt.title("Moore's Law: Transistor Count Over Time", fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Transistor Count (Log Scale)', fontsize=12)
plt.grid(True, which="both", linestyle="--", alpha=0.5)


plt.savefig('moores_law_simple.png')