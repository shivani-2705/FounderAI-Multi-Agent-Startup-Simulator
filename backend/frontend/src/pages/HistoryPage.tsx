import { useParams } from "react-router-dom";

export default function HistoryPage() {

    const { projectId } = useParams();

    return (
        <div>

            <h1>
                History
            </h1>

            <p>
                Project:
            </p>

            <code>
                {projectId}
            </code>

        </div>
    );

}