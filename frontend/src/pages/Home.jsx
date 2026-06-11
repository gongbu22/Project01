import { useState } from "react";

import ChatBox from "../components/ChatBox";
import AnswerBox from "../components/AnswerBox";

import { sendMessage } from "../api/chatApi";

export default function Home() {
  const [message, setMessage] = useState("");

  const [answer, setAnswer] = useState("");

  const handleSend = async () => {
    const result = await sendMessage(message);

    setAnswer(result.answer);
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

    </div>
  );

}