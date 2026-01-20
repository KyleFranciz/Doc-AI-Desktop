import { HomePageI } from "@/routes";
import axios from "axios";

// dummy data
const titleAndPhrasing = { title: "Welcome User,", phrase: "Ready to code?" };

// function to get the data for the hero section
export const getHeroData = () => {
  return titleAndPhrasing;
};
