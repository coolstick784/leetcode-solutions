import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    l_score = list(set(scores.score))
    sorted_score = list(scores.score)
    sorted_score.sort()
    sorted_score.reverse()
    l_score.sort()
    l_score.reverse()
    f_scores = []
    f_rank = []
    cur_rank = 1
    for score1 in sorted_score:
        if l_score[cur_rank-1] != score1:
            cur_rank += 1
        f_scores.append(score1)
        f_rank.append(cur_rank)
    return pd.DataFrame(list(zip(f_scores, f_rank)), columns = ['score', 'rank'])

           
            
        
