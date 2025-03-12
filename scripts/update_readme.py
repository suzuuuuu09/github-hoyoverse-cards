import os
import glob

GAME_CONFIGS = {
    'gi': {
        'title': 'Genshin Impact',
        'path': 'assets/img/gi/*.png'
    },
    'hsr': {
        'title': 'Honkai: Star Rail',
        'path': 'assets/img/hsr/*.png'
    },
    'zzz': {
        'title': 'Zenless Zone Zero',
        'path': 'assets/img/zzz/*.png'
    }
}

def generate_game_section(game_key):
    """Generate markdown section for a specific game."""
    config = GAME_CONFIGS[game_key]
    image_files = sorted(glob.glob(config['path']), key=lambda x: int(os.path.basename(x).split('.')[0]))
    
    if not image_files:
        return []
    
    content = [f'## {config["title"]}\n']
    content.append('|  |  |')
    content.append('| :---: | :---: |')
    
    for i in range(0, len(image_files), 2):
        img1 = os.path.basename(image_files[i])
        img1_num = img1.split('.')[0]
        
        if i + 1 < len(image_files):
            img2 = os.path.basename(image_files[i + 1])
            img2_num = img2.split('.')[0]
            content.append(f'| ![{img1}]({game_key}/{img1}) | ![{img2}]({game_key}/{img2}) |')
            content.append(f'| {img1_num} | {img2_num} |')
        else:
            content.append(f'| ![{img1}]({game_key}/{img1}) | |')
            content.append(f'| {img1_num} | |')
    
    return content

def generate_readme():
    """Generate the complete README.md with all game sections."""
    all_content = []
    
    for game_key in GAME_CONFIGS:
        section_content = generate_game_section(game_key)
        if section_content:
            all_content.extend(section_content)
            all_content.append('\n')  # Add blank line between sections
    
    if all_content:
        # Remove the last blank line
        if all_content[-1] == '\n':
            all_content.pop()
        
        # Write to README.md
        with open('assets/img/README.md', 'w', encoding='utf-8') as f:
            f.write('\n'.join(all_content))

if __name__ == '__main__':
    generate_readme()