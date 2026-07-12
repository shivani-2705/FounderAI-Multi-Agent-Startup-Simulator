type Props = {
    name: string;
    state: "completed" | "running" | "waiting";
};

export default function AgentCard({
    name,
    state,
}: Props) {
    const icon =
        state === "completed"
            ? "✅"
            : state === "running"
            ? "⏳"
            : "⚪";

    return (
        <div className={`agent-card ${state}`}>
            <span>{icon}</span>

            <span>{name}</span>
        </div>
    );
}