# voiceroid_auto
ボイスロイドソフト自動化のプログラムファイル
　今のところは入力したものをオウム返ししているだけですが、今後対話できるように機能を上げる予定です。

　主に行っていることは、Windows内部の動かしているハンドルの検索を行い、一致したハンドルをもとに操作を行う。
ハンドルを探すものとしてInspectツールを使って内部を見ながら確認しています。
　他にも入力情報をもとにソフトで読み上げる時間や保存する時間のウェイトタイムを計算してその時間を操作不能にすることによって実行途中エラーを防いでいます。送信ボタンを押すと自動でファイルを1からナンバリングして保存しています。
