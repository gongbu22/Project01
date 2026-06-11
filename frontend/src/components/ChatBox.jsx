export default function ChatBox({
  message,
  setMessage,
  onSend
}){

  return (

   <div>
    <textarea value={message}
              onChange={(e)=>setMessage(e.target.value)} >
    </textarea>
    <button onClick={onSend}>
      질문하기
    </button>
   </div>
  
);

}