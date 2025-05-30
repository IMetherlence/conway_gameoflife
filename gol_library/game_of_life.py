from collections import Counter

def read_lif(lif_name:str,liveBoard:set)->set:

    with open(lif_name,'r') as f:
        for lines in f:
            line = lines.strip()

            # Ignore the first line
            if line == "#Life 1.06":
                continue

            x,y = line.split(None,1)
            liveBoard.add((int(x),int(y)))

    return liveBoard

def output_lif(liveBoard:set,filename:str)->str:
    try:
        with open(filename,'w') as f:
            f.write("#Life 1.06\n")

            for x,y in liveBoard:
                f.write(f"{x} {y}\n")
        return f"{filename} successfully written"
    except Exception as e:
        return f"Error: {e}"
    
def lif_iteration(liveBoard:set)->set:
    neighbour_offset = [
        (-1,1), (0,1),(1,1),
        (-1,0),       (1,0),
        (-1,-1),(0,-1),(1,-1) 
    ]

    neighbour_counts = Counter()
    for (x,y) in liveBoard:
        for dx, dy in neighbour_offset:
            neighbour = (x+dx,y+dy)
            neighbour_counts[neighbour] += 1

    outputBoard = set()

    for cell, count in neighbour_counts.items():
        if cell in liveBoard:
            # 2 or 3 neighbours = Survive
            if count == 2 or count == 3:
                outputBoard.add(cell)

        else:
            # 3 neighbours = Birth
            if count == 3:
                outputBoard.add(cell)

    return outputBoard
