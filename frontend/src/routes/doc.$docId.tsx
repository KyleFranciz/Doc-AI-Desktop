import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/doc/$docId")({
  component: SpecificDocument,
});

function SpecificDocument() {
  return <div>Hello "/doc/$docId"!</div>;
}
