import pytube
import ffmpeg

video_url = 'https://www.youtube.com/watch?v=-bMRxQbLUlg' # paste here your Youtube videos' url
youtube = pytube.YouTube(video_url)

video1080 = youtube.streams.filter(file_extension='mp4').filter(res='1080p').all()
audio = youtube.streams.filter(file_extension='mp4').filter(only_audio=True).all()

video1080[0].download(r'C:\%DESKTOPDIR%\video') 
audio[0].download(r'C:\%DESKTOPDIR%\audio') 

input_video =  ffmpeg.input(r'C:\%DESKTOPDIR%\%s.mp4' %(video1080[0].title))
input_audio = ffmpeg.input(r'C:\%DESKTOPDIR%\%s.mp4' %(video1080[0].title))
print("MERGE HERE")
ffmpeg.concat(input_video, input_audio, v=1, a=1).output(r'C:\Users\Josean Maya\Desktop\out.mp4').run()
print("Merge Complete)
