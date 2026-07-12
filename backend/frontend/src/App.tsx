import {
  Routes,
  Route,
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import HomePage from "./pages/HomePage";
import ProjectPage from "./pages/ProjectPage";
import HistoryPage from "./pages/HistoryPage";

export default function App() {
  return (
      <MainLayout>
          <Routes>

              <Route
                  path="/"
                  element={<HomePage />}
              />

              <Route
                  path="/projects/:projectId"
                  element={<ProjectPage />}
              />

              <Route
                  path="/projects/:projectId/history"
                  element={<HistoryPage />}
              />

          </Routes>
      </MainLayout>
  );
}