import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import Navigation from "./components/navigation/Navigation";
import { ThemeProvider } from "@mui/material";
import CustomTheme from "./CustomTheme";

function App() {
  return (
    <ThemeProvider theme={CustomTheme}>
      <Router>
        <Navigation />
      </Router>
    </ThemeProvider>
  );
}

export default App;
