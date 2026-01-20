import { createFileRoute } from "@tanstack/react-router";

import { PromptInput } from "../components/ui/PromptInput";

export const Route = createFileRoute("/chat")({
  component: ChatPage,
});

function ChatPage() {
  return (
    <div className="flex w-full justify-center">
      <PromptInput placeholder="Type your prompt..." />
    </div>
  );
}
