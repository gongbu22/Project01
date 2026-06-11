import { useState } from "react";

import ChatBox from "../components/ChatBox";
import AnswerBox from "../components/AnswerBox";
import UploadBox from "../components/UploadBox";

import { sendMessage } from "../api/chatApi";
import { uploadPdf } from "../api/uploadApi";

export default function Home() {
  const [message, setMessage] = useState("");

  const [answer, setAnswer] = useState("");

  const handleSend = async () => {
    const result = await sendMessage(message);

    setAnswer(result.answer);
  };

  const handleUpload = async (file) => {
    const result = await uploadPdf(file);

    console.log(result);
  };

  return (
    <div>

      <ChatBox
        message={message}
        setMessage={setMessage}
        onSend={handleSend}
      >
      </ChatBox>

      <AnswerBox
        answer={answer}>
      </AnswerBox>

      <UploadBox  
        onUpload={handleUpload}>
      </UploadBox>

    </div>
  );

}