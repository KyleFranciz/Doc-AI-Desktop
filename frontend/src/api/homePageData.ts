import { HomePageI } from "@/routes";
import axios from "axios";

// dummy data
const titleAndPhrasing = {
  title: "Welcome Kyle,",
  phrase: "Need help understanding something?",
};

// function to get the data for the hero section
export const getHeroData = () => {
  return titleAndPhrasing;
};
