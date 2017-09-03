import player as pl
import chessmap as ch_map

def init_server():
	pl.init_player()



def main():
	init_server()

	roundno = 1
	while(true):
		end = true
		for player_id in range(1, 5):
			action = pl.run(player_id)
			if action is no null:
				end = false
				print "player:%d, action: %d", player_id, action.chess_id
				ch_map.update_chessmap(player_id, action)
				pl.update_chess_use_info(player_id, chess_id)
				pl.update_candidate_points(player_id, action)

		if end == true:
			print "Game Over!"
			break

if __name__ == '__main__':

	print "server start!"

	main()