interface Props {
    progress: number;
}

export default function ProgressBar({
    progress,
}: Props) {

    return (

        <div
            style={{
                width: "100%",
                background: "#ddd",
                borderRadius: 8,
                overflow: "hidden",
                marginTop: 20,
            }}
        >

            <div
                style={{
                    width: `${progress}%`,
                    height: 12,
                    background: "#2563eb",
                    transition: "0.4s",
                }}
            />

            <p>

                {progress}%

            </p>

        </div>

    );

}