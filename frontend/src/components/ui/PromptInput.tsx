import * as React from "react";

import { ArrowUpIcon } from "./chadcn/arrow-up";
import { cn } from "../../lib/utils";
import { AttachFileIcon } from "./chadcn/attach-file";
import { MicIcon } from "./chadcn/mic";

export interface PromptInputProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}

const PromptInput = React.forwardRef<HTMLTextAreaElement, PromptInputProps>(
  ({ className, onInput, ...props }, ref) => {
    const textareaRef = React.useRef<HTMLTextAreaElement>(null);

    React.useImperativeHandle(
      ref,
      () => textareaRef.current as HTMLTextAreaElement,
    );

    // function that handles auto adjust for the sizing
    const handleInput = (event: React.FormEvent<HTMLTextAreaElement>) => {
      const target = event.currentTarget;
      target.style.height = "auto";
      target.style.height = `${target.scrollHeight}px`;
      onInput?.(event);
    };

    // onClick function to send the data to the backend with a mutation

    return (
      <div className="relative w-full max-w-189.5">
        <textarea
          ref={textareaRef}
          className={cn(
            "min-h-36 w-full resize-none overflow-hidden rounded-3xl border border-[#474747] bg-background px-4 py-4 pb-20 text-base text-foreground placeholder:text-foreground placeholder:opacity-70 hover:border-[#666666] focus-visible:outline-none ",
            className,
          )}
          onInput={handleInput}
          {...props}
        />
        <button
          className="absolute bottom-4 right-3 flex h-10 w-10 items-center justify-center rounded-full bg-[#0F9E6A] hover:cursor-pointer"
          type="button"
          aria-label="Submit prompt"
        >
          <ArrowUpIcon className="text-[#171717]" size={25} />
        </button>
        <div className="absolute bottom-4 left-3 flex flex-row gap-1">
          <button className="h-10 w-10 flex items-center justify-center rounded-lg border-[#474747] border bg-background hover:cursor-pointer">
            <AttachFileIcon className="" size={25} />
          </button>
          <button className="h-10 w-10 flex items-center justify-center rounded-lg border-[#474747] border bg-background hover:cursor-pointer">
            <MicIcon className="" size={25} />
          </button>
        </div>
      </div>
    );
  },
);

PromptInput.displayName = "PromptInput";

export { PromptInput };
