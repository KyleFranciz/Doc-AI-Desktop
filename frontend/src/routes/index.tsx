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
  // function is set up to get dummy data for now (planning to keep title and phrase local and return based on time)
  const { data, error } = useQuery<HomePageI>({
    queryKey: ["homePageData"],
    queryFn: () => getHeroData(),
  });
  return (
    <div className="h-screen flex flex-col justify-center ">
      <div className=" flex flex-col items-center w-full text-2xl xl:text-[2.8vw] lg:text-[3.1vw] md:text-[3.8vw] sm:text-[3.5vw] xs:text-[4.5vw] gap-0 mb-9 ">
        <h1 className="font-instrument-serif titles ">{data?.title}</h1>
        <h2 className="font-instrument-serif titles ">{data?.phrase}</h2>
      </div>
      <div className="mt-7 flex w-full justify-center">
        <PromptInput placeholder="What do you need help with?" />
      </div>
    </div>
  );
}
