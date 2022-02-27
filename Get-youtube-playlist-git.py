#-*- coding: utf-8 -*-

from apiclient.discovery import build

#取得したAPIキー
API_KEY = "AIzaSyDSrWaTNNRovxW8ZCdZ1fHgz5cN7pGjSus"
#対象のプレイリストID
PLAYLIST = "PLg9aIQcFDtaiCto6WAWy0v0mj-IZUOT8l"
#動画数（1～50を指定可能）
MAX_RESULT = 50

#特定プレイリストの動画名，URLを出力する（上限50個）
def youtube_search():
    youtube = build("youtube", "v3", developerKey=API_KEY)

    search_response = youtube.playlistItems().list(
      playlistId=PLAYLIST,
      part="id,snippet",
      maxResults=MAX_RESULT
    ).execute()

    videos = []
    for search_result in search_response.get("items", []):
        #if search_result["id"]["kind"] == "youtube#playlistItemListResponse ":
          videos.append("%s (https://www.youtube.com/watch?v=%s)" % (search_result["snippet"]["title"],
                                     search_result["snippet"]["resourceId"]["videoId"]))

    print("\n".join(videos))

if __name__ == "__main__":
    youtube_search()
