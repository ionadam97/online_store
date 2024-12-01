import { createTheme } from "@mui/material/styles";

const CustomTheme = createTheme({
  palette: {
    mode: "light",
    primary: {
      main: "#0D58D9",
      light: "#0644B8",
      dark: "#0033A0",
    },
    secondary: {
      main: "#d50000",
      light: "#c62828",
      dark: "#b71c1c",
      transparent: "#ef9a9a",
    },
    divider: "#0D58D9",
  },
  typography: {
    h1: {
      fontSize: "3rem",
      fontWeight: 700,
    },
    h2: {
      fontSize: "2.25rem",
      fontWeight: 700,
    },
    h3: {
      fontSize: "1.75rem",
      fontWeight: 600,
    },
    h4: {
      fontSize: "1.5rem",
    },
    h5: {
      fontSize: "1.25rem",
    },
    h6: {
      fontSize: "1.125rem",
    },
  },
  components: {
    MuiButton: {
      variants: [
        {
          props: { variant: "contained" },
          style: {
            fontSize: "1.2rem",
            borderRadius: 30,
            textTransform: "none",
            backgroundColor: "primary.main",
            "&:hover": {
              backgroundColor: "primary.light",
            },
          },
        },
        {
          props: { variant: "containedRed" },
          style: {
            fontSize: "1.2rem",
            borderRadius: 30,
            textTransform: "none",
            color: "white",
            backgroundColor: "#d50000",
            "&:hover": {
              backgroundColor: "#c62828",
            },
            "&.Mui-disabled": {
              background: "rgba(0, 0, 0, 0.12)",
              color: "rgba(0, 0, 0, 0.26)",
            },
          },
        },
        {
          props: { variant: "outlined" },
          style: {
            fontSize: "1.2rem",
            borderRadius: 30,
            textTransform: "none",
            borderColor: "primary.main",
            "&:hover": {
              backgroundColor: "primary.light",
            },
          },
        },
        {
          props: { variant: "outlinedRed" },
          style: {
            fontSize: "1.2rem",
            borderRadius: 30,
            textTransform: "none",
            color: "#d50000",
            border: "1px solid",
            "&:hover": {
              color: "#c62828",
              borderColor: "#c62828",
              backgroundColor: "#ef9a9a",
            },
            "&.Mui-disabled": {
              borderColor: "rgba(0, 0, 0, 0.12)",
            },
          },
        },
        {
          props: { variant: "rounded" },
          style: {
            fontSize: "1.2rem",
            borderRadius: 4,
            textTransform: "none",
          },
        },
      ],
    },
  },
});

export default createTheme(CustomTheme);
