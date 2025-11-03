async function trier() {
    const algo = document.getElementById("algo").value;
    const array = document.getElementById("array").value
        .split(",")
        .map(x => parseInt(x.trim()));

    const res = await fetch("/sort", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ algorithm: algo, array: array })
    });

    const data = await res.json();
    const steps = data.steps;
    await visualiser(steps);
}

async function visualiser(steps) {
    const container = document.getElementById("visualisation");
    for (let step of steps) {
        container.innerHTML = "";
        for (let val of step) {
            const bar = document.createElement("div");
            bar.className = "bar";
            bar.style.height = `${val * 20}px`;
            container.appendChild(bar);
        }
        await new Promise(r => setTimeout(r, 200));
    }
}
