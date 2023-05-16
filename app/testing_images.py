import os
# {'Case': {'Case3': ['NZXT H5 Elite Compact ATX Mid Tower PC Gaming Case(white)', '140', '4.7'], 'Case8': ['KEDIERS
# PC Case Full Tower(white)', '126', '4.0'], 'Case6': ['SZSKYING Gaming ATX PC Case Full Tower (Black)', '150',
# '4.1'], 'Case5': ['Segotep T1 Full Tower E ATX Gaming PC Case (Black)', '180', '4.6'], 'Case1': ['Corsair 4000D
# Airflow Tempered Glass Mid Tower ATX PC Case Black', '95', '4.8'], 'Case4': ['GIM ATX Mid Tower Case White Gaming
# PC Case', '136', '4.5'], 'Case2': ['GIM ATX Mid Tower Case Black Gaming PC Case 2 Tempered Glass Panels & Front
# Panel RGB Strip Gaming Computer Case', '136', '4.5'], 'Case7': ['Lian Li LI PC O11 Dynamic EVO Snow White ATX Full
# Tower Gaming Computer Case', '185', '4.8']}, 'Cooler': {'Cooler1': ['Kit Water cooling Antec Symphony 240 ARGB
# 240mm (Noir) Black', '145', '4.9'], 'Cooler4': ['DeepCool AK620 CPU Air Cooler', '65', '4.7'], 'Cooler5': [
# 'DeepCool AK620 WH CPU Air Cooler', '70', '4.7'], 'Cooler2': ['Thermaltake TH120 ARGB Sync All in One 120mm Liquid
# Cooler(Black)', '85', '4.1'], 'Cooler3': ['Vetroo V360 White Liquid CPU Cooler, 3X 120mm Addressable RGB', '120',
# '4.6']}, 'CPU': {'CPU5': ['AMD Ryzen 3 4100', '65', '4.3'], 'CPU2': ['AMD Ryzen 7 5700G', '187', '4.7'],
# 'CPU4': ['AMD Ryzen 5 5600G', '127', '4.7'], 'CPU3': ['Intel Core i5 13600KF', '294', '4.9'], 'CPU1': ['Intel Core
# i9 10900k', '341', '4.2']}, 'GPU': {'GPU1': ['ASUS TUF Gaming NVIDIA GeForce RTX 3060 V2 OC Edition Graphics Card',
# '400', '4.7'], 'GPU5': ['ASUS TUF Gaming GeForce RTX® 4080 Graphics Card', '1200', '4.5'], 'GPU2': ['GIGABYTE
# GeForce RTX 3070 Gaming OC 8G', '500', '4.6'], 'GPU3': ['ZOTAC Gaming GeForce RTX 4070 Ti Trinity', '800', '4.8'],
# 'GPU4': ['MSI Gaming GeForce RTX 4090', '1650', '4.4']}, 'MB': {'MB4': ['MSI MPG Z490 Gaming Plus Gaming
# Motherboard (ATX, 10th Gen Intel Core)', '125', '4.6'], 'MB3': ['MSI MEG Z790 ACE Gaming Motherboard Supports 12th
# and 13th Gen Intel Processors', '500', '4.4'], 'MB5': ['ASUS AM4 TUF Gaming X570 Plus (WiFi) AM4 Zen 3 Ryzen 5000 &
# 3rd Gen Ryzen ATX Motherboard', '210', '4.3'], 'MB1': ['ASUS AM4 TUF Gaming X570 Plus (WiFi) AM4 Zen 3 Ryzen 5000 &
# 3rd Gen Ryzen ATX Motherboard', '210', '4.7'], 'MB2': ['GIGABYTE B550M DS3H AC AM4 AMD', '120', '4.5']},
# 'Power': {'Power2': ['750W Fully Modular RGB Power Supply', '80', '4.5'], 'Power4': ['Apevia ATX PR800W Prestige
# 800W', '67', '4.5'], 'Power3': ['Redragon PSU007 80+ Gold 850 Watt', '120', '4.6'], 'Power1': ['Corsair RMX Series
# (2021), RM1000x, 1000 Watt, Gold', '189', '4.7'], 'Power5': ['ARESGAME AGV Series 750W Power Supply', '70',
# '4.6']}, 'Ram': {'Ram2': ['Corsair Vengeance LPX 32GB (2X16GB) DDR4 3200(Black)', '65', '4.8'], 'Ram1': ['TEAMGROUP
# T Force Delta RGB DDR4 64GB (2x32GB) 3600MHz(White)', '140', '4.8'], 'Ram4': ['Corsair Vengeance RGB Pro 32GB (
# 2x16GB) DDR4 3200(Black)', '80', '4.8'], 'Ram3': ['Corsair Vengeance RGB Pro SL 32GB (2x16GB) DDR4 3600(White)',
# '100', '4.8'], 'Ram5': ['TEAMGROUP T Force Vulcan DDR5 32GB (2x16GB) 5200MHz(Black)', '90', '4.5']}, 'Storage': {
# 'Storage1': ['Samsung 970 EVO Plus SSD 2TB NVMe M.2 Internal Solid State Hard Drive', '130', '4.8'], 'Storage4': [
# 'SAMSUNG Electronics 870 EVO 2TB 2.5 Inch SATA III Internal SSD', '120', '4.8'], 'Storage3': ['fanxiang S500 Pro
# 2TB NVMe SSD M.2', '80', '4.5'], 'Storage6': ['Western Digital 1TB WD Blue SA510 SATA Internal Solid State Drive
# SSD', '54', '4.7'], 'Storage5': ['TEAMGROUP T Force Vulcan Z 1TB SLC Cache 3D NAND TLC 2.5 Inch SATA III Internal
# Solid State Drive SSD', '40', '4.7'], 'Storage2': ['TEAMGROUP MS30 512GB with SLC Cache 3D NAND TLC M.2', '21',
# '4.6']}}


folder_dir = '/Users/sayedulislam/microblog/app/static/images'
parts = {"Case": {}, "Cooler": {}, "CPU": {}, "GPU": {}, "MB": {}, "Power": {}, "Ram": {}, "Storage": {}}

for filename in os.listdir(folder_dir):
    if filename.endswith(".png"):
        # extract the part name and image filename from the file name
        name = os.path.splitext(filename)[0]

        img_name = name.split('-')
        name2 = img_name[0]
        par = name2[:-1]

        parts[par][filename] = [img_name[1]]
        parts[par][filename] += [img_name[2]]
        parts[par][filename] += [img_name[3]]


print(parts)


preBuild = {'Gaming': {}, 'Business': {}, 'Video Editing': {}, 'Everyday': {}}


folder_prebuilt = '/Users/sayedulislam/microblog/app/static/prebuilt'
for filename in os.listdir(folder_prebuilt):
    if filename.endswith(".png"):
        # extract the part name and image filename from the file name
        name = os.path.splitext(filename)[0]

        img_name = name.split('-')
        par = img_name[0]

        preBuild[par][filename] = [img_name[1]]  # name of pc
        preBuild[par][filename] += [img_name[2]]  # Price
        preBuild[par][filename] += [img_name[3]]  # rating
        preBuild[par][filename] += [img_name[4]]  # Processor Type
        preBuild[par][filename] += [img_name[5]]  # Disk Size
        preBuild[par][filename] += [img_name[6]]  # RAM
        preBuild[par][filename] += [img_name[7]]  # Processor Speed
        preBuild[par][filename] += [img_name[8]]  # GPU


print(preBuild)


# {'Gaming': {'Gaming-Lenovo IdeaCentre 5 Gaming Desktop-$1200-4.3 out of 5 rating-Processor Type: Core i7-Disk Size: 512 GB-RAM: 32 GB-Processor Speed: 1.60 GHz-GPU: GeForce RTX 3060.png': ['Lenovo IdeaCentre 5 Gaming Desktop', '$1200', '4.3 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 512 GB', 'RAM: 32 GB', 'Processor Speed: 1.60 GHz', 'GPU: GeForce RTX 3060'], 'Gaming-Alienware Aurora R10 Gaming Desktop-$1600-4.4 out of 5 rating-Processor Type: AMD Ryzen 7-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 4.6 GHz-GPU: NIVIDIA GeForce RTX 3080 LHR.png': ['Alienware Aurora R10 Gaming Desktop', '$1600', '4.4 out of 5 rating', 'Processor Type: AMD Ryzen 7', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 4.6 GHz', 'GPU: NIVIDIA GeForce RTX 3080 LHR'], 'Gaming-Lenovo Legion Tower 5i Gaming Desktop-$999-4.4 out of 5 rating-Processor Type: Core i7-Disk Size: 2 TB-RAM: 32 GB-Processor Speed: 2.10 GHz-GPU: NVIDIA GeForce RTX 3070.png': ['Lenovo Legion Tower 5i Gaming Desktop', '$999', '4.4 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 2 TB', 'RAM: 32 GB', 'Processor Speed: 2.10 GHz', 'GPU: NVIDIA GeForce RTX 3070'], 'Gaming-Alienware Aurora R12-$1700-4.8 out of 5 rating-Processor Type: Core i7-Disk Size: 256 GB-RAM: 16 GB-Processor Speed: 3 GHz-GPU: GeForce RTX 3070.png': ['Alienware Aurora R12', '$1700', '4.8 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 256 GB', 'RAM: 16 GB', 'Processor Speed: 3 GHz', 'GPU: GeForce RTX 3070'], 'Gaming-Lenovo Legion Tower T5 Gaming Desktop-$1359-4.6 out of 5 rating-Processor Type: Core i7-Disk Size: 1 TB-RAM: 64 GB-Processor Speed: 2.50 GHz-GPU: GeForce RTX 3060.png': ['Lenovo Legion Tower T5 Gaming Desktop', '$1359', '4.6 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 1 TB', 'RAM: 64 GB', 'Processor Speed: 2.50 GHz', 'GPU: GeForce RTX 3060'], 'Gaming-Alienware Aurora R15 Gaming Desktop-$3550-4.5 out of 5 rating-Processor Type: Ryzen 9-Disk Size: 2 TB-RAM: 32 GB-Processor Speed: 5.6 GHz-GPU: NIVIDIA GeForce RTX 4080.png': ['Alienware Aurora R15 Gaming Desktop', '$3550', '4.5 out of 5 rating', 'Processor Type: Ryzen 9', 'Disk Size: 2 TB', 'RAM: 32 GB', 'Processor Speed: 5.6 GHz', 'GPU: NIVIDIA GeForce RTX 4080']}, 'Business': {'Business-Dell Inspiron 3910 Desktop Computer Tower-$647-4.4 out of 5 rating-Processor Type: Core i5-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 4.4 GHz-GPU: Intel UHD Graphics 730.png': ['Dell Inspiron 3910 Desktop Computer Tower', '$647', '4.4 out of 5 rating', 'Processor Type: Core i5', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 4.4 GHz', 'GPU: Intel UHD Graphics 730'], 'Business-Dell OptiPlex 7000 Series 7090 Tower Business Desktop-$990-4.7 out of 5 rating-Processor Type: Core i7-Disk Size: 1 TB-RAM: 32 GB-Processor Speed: 2.50 GHz-GPU: Intel UHD Graphics 750.png': ['Dell OptiPlex 7000 Series 7090 Tower Business Desktop', '$990', '4.7 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 1 TB', 'RAM: 32 GB', 'Processor Speed: 2.50 GHz', 'GPU: Intel UHD Graphics 750'], 'Business-HP ENVY Desktop Computer-$950-4.4 out of 5 rating-Processor Type: Core i7-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 4.8 GHz-GPU: Inegrated.png': ['HP ENVY Desktop Computer', '$950', '4.4 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 4.8 GHz', 'GPU: Inegrated'], 'Business-Dell OptiPlex 7080 Micro Form Factor Mini Business Desktop-$680-4.0 out of 5 rating-Processor Type: Core i5-Disk Size: 1 TB-RAM: 32 GB-Processor Speed: 2.30 GHz-GPU: Intel UHD Graphics.png': ['Dell OptiPlex 7080 Micro Form Factor Mini Business Desktop', '$680', '4.0 out of 5 rating', 'Processor Type: Core i5', 'Disk Size: 1 TB', 'RAM: 32 GB', 'Processor Speed: 2.30 GHz', 'GPU: Intel UHD Graphics'], 'Business-HP Pavilion Desktop PC-$760-4.4 out of 5 rating-Processor Type: AMD Ryzen 7 5700G-Disk Size: 512 GB-RAM: 16 GB-Processor Speed: 3.8 GHz-GPU: AMD Radeon.png': ['HP Pavilion Desktop PC', '$760', '4.4 out of 5 rating', 'Processor Type: AMD Ryzen 7 5700G', 'Disk Size: 512 GB', 'RAM: 16 GB', 'Processor Speed: 3.8 GHz', 'GPU: AMD Radeon'], 'Business-HP ProDesk 400 G7 Tower Business Desktop-$650-4.3 out of 5 rating-Processor Type: Core i5-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 3.10 GHz-GPU: Intel UHD Graphics.png': ['HP ProDesk 400 G7 Tower Business Desktop', '$650', '4.3 out of 5 rating', 'Processor Type: Core i5', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 3.10 GHz', 'GPU: Intel UHD Graphics']}, 'Video Editing': {'Video Editing-ASUS ROG GT15CF Gaming Desktop Computer-$1300-4.4 out of 5 rating-Processor Type: Core i9-Disk Size: 4512 GB-RAM: 64 GB-Processor Speed:3.20 GHz-GPU: NVIDIA GeForce RTX 3060.png': ['ASUS ROG GT15CF Gaming Desktop Computer', '$1300', '4.4 out of 5 rating', 'Processor Type: Core i9', 'Disk Size: 4512 GB', 'RAM: 64 GB', 'Processor Speed:3.20 GHz', 'GPU: NVIDIA GeForce RTX 3060'], 'Video Editing-ASUS Newest ROG Strix GL10 Premium Gaming Desktop-$900-4.2 out of 5 rating-Processor Type: AMD R Series-Disk Size: 1000 GB-RAM:32 GB-Processor Speed:3 GHz-GPU: GeForce GTX 1660.png': ['ASUS Newest ROG Strix GL10 Premium Gaming Desktop', '$900', '4.2 out of 5 rating', 'Processor Type: AMD R Series', 'Disk Size: 1000 GB', 'RAM:32 GB', 'Processor Speed:3 GHz', 'GPU: GeForce GTX 1660'], 'Video Editing-CyberpowerPC Gamer Xtreme VR Gaming PC-$1270-4.5 out of 5 rating-Processor Type: Core i7-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 2.1 GHz-GPU: NIVIDIA GeForce GTX 3060.png': ['CyberpowerPC Gamer Xtreme VR Gaming PC', '$1270', '4.5 out of 5 rating', 'Processor Type: Core i7', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 2.1 GHz', 'GPU: NIVIDIA GeForce GTX 3060'], 'Video Editing-2022 Newest ASUS ROG Strix GL10 Gaming Desktop-$815-4.1 out of 5 rating-Processor Type: Ryzen 5 3600X-Disk Size: 512 GB-RAM: 16 GB-Processor Speed:3.8 GHz-GPU: GeForce GTX 1660 Ti.png': ['2022 Newest ASUS ROG Strix GL10 Gaming Desktop', '$815', '4.1 out of 5 rating', 'Processor Type: Ryzen 5 3600X', 'Disk Size: 512 GB', 'RAM: 16 GB', 'Processor Speed:3.8 GHz', 'GPU: GeForce GTX 1660 Ti'], 'Video Editing-CyberpowerPC Gamer Xtreme VR Gaming PC-$1200-4.6 ot of 5 rating-Processor Type: Core i5-Disk Size: 1 TB-RAM: 8 GB-Processor Speed: 2.9 GHz-GPU: NVIDIA GeForce GTX 1660.png': ['CyberpowerPC Gamer Xtreme VR Gaming PC', '$1200', '4.6 ot of 5 rating', 'Processor Type: Core i5', 'Disk Size: 1 TB', 'RAM: 8 GB', 'Processor Speed: 2.9 GHz', 'GPU: NVIDIA GeForce GTX 1660'], 'Video Editing-CYBERPOWERPC Gamer Xtreme VR Gaming PC-$950-4.5 out of 5 rating-Processor Type: Core i5-Disk Size: 500 GB-RAM: 8 GB-Processor Speed:2.5 GHz-GPU: GeForce RTX 3050.png': ['CYBERPOWERPC Gamer Xtreme VR Gaming PC', '$950', '4.5 out of 5 rating', 'Processor Type: Core i5', 'Disk Size: 500 GB', 'RAM: 8 GB', 'Processor Speed:2.5 GHz', 'GPU: GeForce RTX 3050']}, 'Everyday': {'Everyday-Corsair ONE i200 Compact Gaming PC-$3100-4.8 out of 5 rating-Processor Type: Intel Core i7-Disk Size: 1 TB-RAM: 32.0 GB-Processor Speed:3.6 GHz-GPU: GeForce TRX 3080.png': ['Corsair ONE i200 Compact Gaming PC', '$3100', '4.8 out of 5 rating', 'Processor Type: Intel Core i7', 'Disk Size: 1 TB', 'RAM: 32.0 GB', 'Processor Speed:3.6 GHz', 'GPU: GeForce TRX 3080'], 'Everyday-Corsair ONE a200 Compact Gaming PC-$2600-4.4 out of 5 rating-Processor Type: AMD Ryzen 9 5900X-Disk Size: 1 TB-RAM: 32.0 GB-Processor Speed:3.7 GHz-GPU: GeForce RTX 3080.png': ['Corsair ONE a200 Compact Gaming PC', '$2600', '4.4 out of 5 rating', 'Processor Type: AMD Ryzen 9 5900X', 'Disk Size: 1 TB', 'RAM: 32.0 GB', 'Processor Speed:3.7 GHz', 'GPU: GeForce RTX 3080'], 'Everyday-Thermaltake Graphite 360 Gaming PC-$1200-4.1 ot of 5 rating-Processor Type: AMD Ryzen 5 5600X-Disk Size: 1 TB-RAM: 16 GB-Processor Speed:3.7 GHz-GPU: GeForce RTX 3060.png': ['Thermaltake Graphite 360 Gaming PC', '$1200', '4.1 ot of 5 rating', 'Processor Type: AMD Ryzen 5 5600X', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed:3.7 GHz', 'GPU: GeForce RTX 3060'], 'Everyday-Thermaltake View 380 Liquid Cooled PC-$2800-3.9 out of 5 rating-Processor Type: AMD Ryzen 7 5800X-Disk Size: 1 TB-RAM: 16 GB-Processor Speed:3.8 GHz-GPU: GeForce RTX 3080.png': ['Thermaltake View 380 Liquid Cooled PC', '$2800', '3.9 out of 5 rating', 'Processor Type: AMD Ryzen 7 5800X', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed:3.8 GHz', 'GPU: GeForce RTX 3080'], 'Everyday-Thermaltake AH-370 Liquid Cooled PC-$1800-4.1 out of 5 rating-Processor Type: Ryzen 7 3700X-Disk Size: 1 TB-RAM: 16 GB-Processor Speed: 3.6 GHz-GPU: GeForce RTX 3070.png': ['Thermaltake AH', '370 Liquid Cooled PC', '$1800', '4.1 out of 5 rating', 'Processor Type: Ryzen 7 3700X', 'Disk Size: 1 TB', 'RAM: 16 GB', 'Processor Speed: 3.6 GHz'], 'Everyday-Corsair Vengeance i7400 Series Gaming PC-$1700-4.3 out of 5 rating-Processor Type: Core i5-Disk Size: 1 TB -RAM: 16 GB-Processor Speed:3.4 GHz-GPU: GeForce RTX 3060.png': ['Corsair Vengeance i7400 Series Gaming PC', '$1700', '4.3 out of 5 rating', 'Processor Type: Core i5', 'Disk Size: 1 TB ', 'RAM: 16 GB', 'Processor Speed:3.4 GHz', 'GPU: GeForce RTX 3060']}}






