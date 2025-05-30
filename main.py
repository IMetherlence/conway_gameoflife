from gol_library.game_of_life import read_lif,output_lif,lif_iteration

def main():
    inputiterations = int(input("Please key in the number of expected iterations:"))
    inputlif = "./resource/input1.lif"
    # Initialize a set for live cells, assume all other cells are dead
    liveCells = set()
    liveCells = read_lif(inputlif,liveCells)

    for i in range(inputiterations):
        liveCells = lif_iteration(liveCells)
        output_lif(liveCells,f"generation{i+1}.lif")

    print(f"{inputiterations} iteration(s) completed. Please check /output folder.")


if __name__ == '__main__':
    main()