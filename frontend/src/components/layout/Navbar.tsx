// imports

import { PanelLeftOpenIcon } from "../ui/shadcn/panel-left-open";

// Navbar component
export function Navbar() {
  return (
    <div className="flex flex-col ">
      <div className="mt-3.5 px-20 fixed flex w-screen">
        <nav className="cursor-pointer">
          <PanelLeftOpenIcon size={30} className="opacity-80" />
        </nav>
      </div>
      <hr className="h-0.2 fixed mt-14 bg-white opacity-18 w-screen" />
    </div>
  );
}
