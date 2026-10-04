import json
import os

from Main import run_agent


def load_benchmark():
    with open("data/benchmark.json", "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_result(result):
    claims = result["verification"]["claims"]

    total_claims = len(claims)

    supported_claims = sum(
        1 for claim in claims
        if claim["supported"]
    )

    unsupported_claims = total_claims - supported_claims

    if total_claims > 0:
        support_rate = supported_claims / total_claims
    else:
        support_rate = 0

    return {
        "total_claims": total_claims,
        "supported_claims": supported_claims,
        "unsupported_claims": unsupported_claims,
        "support_rate": support_rate,
        "refinement_attempts": result["retry_count"]
    }


def main():
    benchmark = load_benchmark()

    results = []

    for task in benchmark:
        print(f"\nRunning {task['id']}...")

        try:
            result = run_agent(task["question"])

            metrics = evaluate_result(result)

            results.append({
                "id": task["id"],
                "category": task["category"],
                "question": task["question"],
                "status": "completed",
                "answer": result["answer"],
                "retrieved_sources": [
                    source["source_id"]
                    for source in result["evidence"]
                ],
                "verification": result["verification"],
                "metrics": metrics
            })

            print(
                f"Claims: {metrics['total_claims']} | "
                f"Supported: {metrics['supported_claims']} | "
                f"Support rate: {metrics['support_rate']:.2%}"
            )

        except Exception as e:
            results.append({
                "id": task["id"],
                "category": task["category"],
                "question": task["question"],
                "status": "error",
                "error": str(e)
            })

            print(f"ERROR: {e}")

    os.makedirs("results", exist_ok=True)

    with open(
        "results/evaluation_results.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("\nBenchmark complete.")
    print("Results saved to:")
    print("results/evaluation_results.json")


if __name__ == "__main__":
    main()