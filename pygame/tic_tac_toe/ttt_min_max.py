## author: vladimir kulyukin

def read_ttt_min_max_tree(fp):
    ttt_state_table = {}
    with open(fp) as game_states:
        for line in game_states:
            line_splits = [s.strip() for s in line.split(';')]
            ttt_board_state = line_splits[0]
            ttt_state_table[ttt_board_state] = line_splits[1:]
    return ttt_state_table

def get_ttt_min_max_utility(board_state, player, ttt_min_max_tbl):
    utils = ttt_min_max_tbl[board_state]
    tbl_player = utils[0]
    if tbl_player == player:
        if player == 'X':
            return get_ttt_max_utility_move(utils[1])
        elif player == 'O':
            return get_ttt_min_utility_move(utils[1])
        else:
            return None
    else:
        return None

def get_ttt_max_utility_move(utils):
    util_tbl = {}
    for move_util_pair in utils.split(' '):
        m, u = move_util_pair.split(':')
        mkey, uval = int(m), int(u)
        if util_tbl.has_key(uval):
            util_tbl[uval].append(mkey)
        else:
            util_tbl[uval] = [mkey]
    if util_tbl.has_key(1):
        return util_tbl[1][0]
    elif util_tbl.has_key(0):
        return util_tbl[0][0]
    elif util_tbl.has_key(-1):
        return util_tbl[-1][0]
    else:
        return None

def get_ttt_min_utility_move(utils):
    util_tbl = {}
    for move_util_pair in utils.split(' '):
        m, u = move_util_pair.split(':')
        mkey, uval = int(m), int(u)
        if util_tbl.has_key(uval):
            util_tbl[uval].append(mkey)
        else:
            util_tbl[uval] = [mkey]
    if util_tbl.has_key(-1):
        return util_tbl[-1][0]
    elif util_tbl.has_key(0):
        return util_tbl[0][0]
    elif util_tbl.has_key(-1):
        return util_tbl[1][0]
    else:
        return None
