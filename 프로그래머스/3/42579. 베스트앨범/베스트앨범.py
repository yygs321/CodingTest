import collections
import heapq


def solution(genres, plays):
    # 음악 정보를 담는 사전 자료형.
    musics = collections.defaultdict(list)
    
    # 음수 재생 횟수와 인덱스를 튜플로 같이 사전에 삽입.
    # heapq 모듈은 항상 오름차순이기 때문에 재생 횟수를 음수화.
    for index, genre in enumerate(genres):
        heapq.heappush(musics[genre], (-plays[index], index))
    
    # 음수 재생 횟수의 합이기 때문에 역순으로 정렬.
    played_genres = [(sum([-played_count[0] for played_count in played_counts]), genre) for genre, played_counts in musics.items()]
    played_genres.sort(reverse=True)
    
    answer = []
    # 간단하게 heappop 메서드로 가장 많이 재생된(또는 인덱스가 빠른) 노래 추출.
    for _, genre in played_genres:        
        answer.append(heapq.heappop(musics[genre])[1])
        if musics[genre]:
            answer.append(heapq.heappop(musics[genre])[1])
    
    return answer