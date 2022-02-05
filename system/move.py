class Move:

    def __init__(self, move: str):
        self.__move = move

    def get_move(self):
        return self.__move


"""
func encodePGN(g *Game) string {
	s := ""
	for _, tag := range g.tagPairs {
		s += fmt.Sprintf("[%s \"%s\"]\n", tag.Key, tag.Value)
	}
	s += "\n"
	for i, move := range g.moves {
		pos := g.positions[i]
		txt := g.notation.Encode(pos, move)
		if i%2 == 0 {
			s += fmt.Sprintf("%d. %s", (i/2)+1, txt)
		} else {
			s += fmt.Sprintf(" %s ", txt)
		}
		if len(g.comments) > i {
			for _, c := range g.comments[i] {
				s += " { " + c + " } "
			}
		}
	}
	s += " " + string(g.outcome)
	return s
}
"""
