import { Route, Routes, Navigate } from "react-router-dom";
import NavBar from "./NavBar";
import Home from "../pages/Home";

const Navigation = () => {
  return (
    <>
      <NavBar />
      <main style={{ paddingTop: "100px" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          {/* <Route path="users" element={<Users />} /> */}
          <Route path="*" element={<Navigate replace to="/" />} />
        </Routes>
      </main>
    </>
  );
};

export default Navigation;
