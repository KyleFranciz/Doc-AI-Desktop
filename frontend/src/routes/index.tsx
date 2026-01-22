import { createFileRoute } from "@tanstack/react-router";
import axios from "axios";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { getHeroData } from "../api/homePageData.ts";
import { PromptInput } from "../components/ui/PromptInput";

export const Route = createFileRoute("/")({
  component: Home,
});

export interface HomePageI {
  title: string;
  phrase: string;
}

function Home() {
  // function gets the dummy data
  const { data, error } = useQuery<HomePageI>({
    queryKey: ["homePageData"],
    queryFn: () => getHeroData(),
  });
  return (
    <div className="h-screen flex flex-col justify-center ">
      <div className=" flex flex-col items-center w-full text-[3vw] lg:text-[2.3vw] md:text-[3.5vw] sm:text-[3.3vw] gap-0 mb-9 ">
        <h1 className="font-instrument-serif titles ">{data?.title}</h1>
        <h2 className="font-instrument-serif titles ">{data?.phrase}</h2>
      </div>
      <div className="mt-6 flex w-full justify-center">
        <PromptInput placeholder="Type your prompt..." />
      </div>
    </div>
  );
}
