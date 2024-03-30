### Overview
This script serves as a convenient tool for generating metadata for collections, tailored for compatibility with www.generatord.io. It may not align with the requirements of other platforms. The script allows users to define trait rarities, specify traits that should not coexist, and even consider the absence of a trait ("none") as a valid option.

_I'm not a developer, but I enjoy creating tools that might simplify life for others. A large portion of this script was created by ChatGPT. Me monkey, me type._

## Features
- **Spreadsheet Creation**: Creates an organized spreadsheet that users can navigate with ease. This setup facilitates the adjustment of trait rarities and creates rules for trait compatibility.

- **Metadata Generation**: Executes the creation of metadata for a predetermined number of collection items, adhering to the user-defined rarities and rules.

- **Validation**: Aims to maintain the logical consistency of traits within each metadata item and throughout the entire collection. The process involves checking for prohibited trait pairings and aiming to adhere to the user's rarity specifications.

- **Statistics and Summary**: Offers a breakdown of trait usage throughout the collection, with distribution and occurrence frequency of each trait. It's crucial to personally verify that the output aligns with your expectations, as the script doesn't guarantee absolute accuracy.

### Requirements
- Python 3.8 or higher
- The `openpyxl` library, essential for managing Excel spreadsheets.

### How to Use
1. **Setting Up Your Environment**:
   - Confirm that Python 3.8 or higher is installed on your system. To check the version run `python --version`. Python can be installed from here: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Install the required `openpyxl` library using the command: `pip install openpyxl`.

2. **Configuration**:
   - All the images of your traits should be placed in a folder called `traits` that is in the current working 
     directory. If you put your traits in a different directory, you can set the `ROOT_DIRECTORY` variable within the 
     script.
   - This directory should have several folders within it, with each folder representing a trait type 
     (e.g. Background, Head, Expression, etc.). The images of each trait are placed within these trait type directories.
   - The trait type folders must be prepended with a number, which indicates the layering order of the images. 
     For example, a folder with the name `2. Body` represents a trait type called `Body` which is second in the 
     layering order of the trait images. `1` is the furthest back trait (i.e. the background), and increasing numbers 
     are layered on top of lower numbers. Below is an example folder structure for a project with 4 trait types. 
    ```
    traits
    ├─ 1. Background
    │  ├─ Yellow.webp
    │  ├─ Blue.webp
    │  ├─ Mint.webp
    │  └─ Pink.webp
    ├─ 2. Body
    │  ├─ Wizard Robes.webp
    │  ├─ Cargo Jacket.webp
    │  ├─ Collared Shirt.webp
    │  └─ Hoodie.webp
    ├─ 3. Head
    │  ├─ Slate.webp
    │  ├─ Yellow.webp
    │  └─ Grey.webp
    └─ 4. Expression
       ├─ Cheeky.webp
       ├─ Blindfold.webp
       ├─ Hearts.webp
       ├─ Glasses.webp
       ├─ Shades.webp
       └─ Crying.webp
    ```

3. **Running the Script**:
   - Initiate the script by executing `python generateorder.py` in your terminal.
   - The script will create a 'traits_info.xlsx' spreadsheet based on your folder structure. This spreadsheet is used 
     to configure how your collection is generated. Everything in the spreadsheet is optional, so you can run the 
     script without adding anything to the spreadsheet, but you will likely want to add rules and rarity to get it to 
     generate the way you want. The following options are available in the spreadsheet
     - `Rarity (%)`: This is how frequently each trait will be generated as a percentage (i.e. a number from 0 to 100).
        The rarity of all traits within a given trait type should add to 100. If no rarities are given, then all traits 
        are used with equal probability
     - `Blacklist`: This can be used to blacklist certain trait combinations. If you have two traits that don't work well
       together, then you can add a blacklist to them, which means they will never generate together. The blacklist is
       a comma separated list of numbers of the traits to blacklist, where the numbers are obtained from the first 
       column (`Number`). For example, lets say you have two traits `Shades` and `Glasses` that don't work when 
       combined with a `Hoodie`. Then look up the numbers assigned to `Shades` and `Glasses` in the first column. If 
       they have numbers 15 and 16, then you would put `15, 16` in the `Blacklist` column for the `Hoodie` trait. 
       NOTE: You could also do the reverse and put the number for `Hoodie` in both the `Glasses` and `Shades` rows to 
       achieve the same outcome
     - `Whitelist`: The whitelist has the same format as the `Blacklist`, and is the opposite of a blacklist. If you 
       whitelist certain traits, then it means that trait will *only* generate with it's whitelisted traits. This is 
       very useful to 'link' together two images that represent the same trait. For example, if you have a hair trait 
       type, but to get the layering to work you had to separate the images into a back and front, where the back image 
       goes behind the head, and the front in front of the head, then you can use whitelists to make sure that each
       back hair trait generates with its corresponding front hair trait
     - `Inscription ID`: If your traits are already inscribed, you can put the inscription ID's for each one in here,
       and the script will generate your `traits.json` file that can be uploaded to 
       [GeneratOrd](https://www.generatord.io)
   - You can delete, add and reorder traits, however, be careful when doing so. The `Number` column is used to 
     associate the `Whitelist` and `Blacklist` columns to the traits, so if you change which numbers correspond to 
     which trait, it may make all of your whitelists and blacklists incorrect

4. **Generating Metadata**:
   - Once you've updated the 'traits_info.xlsx' file, press Enter in your terminal to prompt the script to continue.
   - Specify the quantity of items (inscriptions) for which you intend to generate metadata.
   - The script then creates the metadata generation, ensuring each item is not the same as any other already created 
     for metadata and attempts to abide by rarity, blacklists and whitelists. It concurrently validates the data to 
     identify any inconsistencies or breaks in the rules. It's IMPORTANT to double-check your metadata for precision, as
     discrepancies may exist.

5. **Output**:
   - Upon completion, the script generates several files:
     - `metadata.json`: Houses the metadata for each collection item.
     - `traits.json`: Associates traits with their corresponding inscription IDs.
     - `trait_usage_statistics.json`: Presents a detailed account of trait usage and distribution throughout the collection.

### Handling Errors and Inconsistencies:
- Should you encounter errors or inconsistencies within the 'traits_info.xlsx' file or the generated metadata, the 
  script will highlight these. It's advisable to rectify these based on the provided feedback and re-run the script if 
  necessary.

### Caution
- It's important to ensure that the rules established for rarity and trait avoidance are logically sound. Conflicting 
  or ambiguous rules could hinder the script's ability to produce the collection metadata.

*In scenarios where the script struggles to generate unique metadata for each collection item, it's worthwhile to 
consider introducing additional traits or tweaking the rules to accommodate a broader range of unique combinations.*
