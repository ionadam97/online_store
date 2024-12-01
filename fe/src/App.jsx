import React from "react";
import NavBar from "./components/navigation/NavBar";
import { ThemeProvider } from "@mui/material";
import CustomTheme from "./CustomTheme";

function App() {
  return (
    <>
      <ThemeProvider theme={CustomTheme}>
        <NavBar />


      </ThemeProvider>
    </>
  );
}

export default App;