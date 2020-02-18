//<script type='text/javascript'>

//音声ファイル読み込み
var audioElement;
var count
count = 0;
function start(){
    i = f1();
    audioElement=new Audio();
    audioElement.src="C:/Users/takumi/Desktop/kototalk/"+ i +".wav";
    audioElement.play();
    //alert(i);
}

function f1(){
    count=count+1;
    return count;
}

//出力
function sendButton(){

    you=document.getElementById("output");
    //text=documnent.forms.form1.textBox1
    //document.write(you)
    you.innerText = document.forms.id_form1.id_textBox1.value;
    //you.innerText="test"; .innerTextで表示させる文字をその場で変えることができる
    start()
}
//</script>