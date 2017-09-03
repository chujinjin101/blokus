# player

import json
import os
import random
import chessmap as ch_map

def init_player():
	ch_map.init_chessmap()
	init_chess_use_info()
	init_candidate_points()


chess_use_info = {}
def init_chess_use_info():
	for i in range(0, 4):
		chess_use_info[i] = {101:0,201:0,.....}#already 

candidate_points = {}
def init_candidate_points():
	candidate_points[1] = [{x:0,y:0}]
	candidate_points[2] = [{x:19,y:0}]
	candidate_points[3] = [{x:19,y:19}]
	candidate_points[4] = [{x:0,y:19}]

candidate_actions = {}
def get_candidate_actions():
	all_actions = ch_map.get_all_actions;
	for i in range(1, 5):
		for action in all_actions:
			if !check_if_chess_useed(i, action.chess_id):
				if check_if_action_is_ok():
					candidate_actions.push_back(action)

def check_if_action_is_ok(player_id, action)
	if check_if_can_play_this_chess(action):
		for point in candidate_points[player_id]:
			if check_if_point_in_action(point, action):
				return true
	else:
		return false

def check_if_can_play_this_chess(action):

def check_if_point_in_action(point, action):
	for point_ac in action.points():
		if point == point_ac
			return true

	return false

def update_chess_use_info(player_id, chess_id):
	chess_use_info[int(player_id)][int(chess_id)] = 1

def update_candidate_points(player_id, action):
	# calculate delete candidate points

	# calculate new candidate points

def check_if_chess_useed(player_id, chess_id):
	return chess_use_info[int(player_id)][int(chess_id)]

def run(player_id):
	# get random action from candidate actions
	actions = get_candidate_actions()

	index = 0
	if !actions.empty():
		index = random.randint(0, actions.size())
	else:
		return null

	return actions[index]