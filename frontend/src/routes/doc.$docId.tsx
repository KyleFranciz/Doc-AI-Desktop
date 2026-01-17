import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/doc/$docId')({
  component: RouteComponent,
})

function RouteComponent() {
  return <div>Hello "/doc/$docId"!</div>
}
