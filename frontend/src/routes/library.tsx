import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/library")({
  component: LibraryPage,
});

function LibraryPage() {
  return <div>This is the library page</div>;
}
