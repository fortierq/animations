let k = 3;
let points = [];
let colors = ["red", "green", "blue"];
let circle_nn, input_k;
let sz_point = 20;
let sz = 400;


function setup() {
    createCanvas(sz, sz);
    for (const color of colors)
        for (let i = 0; i < 5; i++) {
            let x = sz * Math.random(), y = sz * Math.random();
            points.push([x, y, color]);
        }
    input_k = createInput("3");
    input_k.position(sz / 2, sz + 10);
    input_k.size(30);
    createElement('h4', 'Valeur de k :').position(sz / 2 - 100, sz - 10);
}

function draw() {
    background(220);
    for (const p of points) {
        fill(p[2]);
        noStroke();
        circle(p[0], p[1], sz_point);
    }
    noFill();
    stroke("black");
    if (circle_nn)
        circle(circle_nn[0], circle_nn[1], circle_nn[2]);
}

function most_frequent(array) {
    let freq = {};
    let max_e;
    for (const e of array) {
        if (!freq[e])
            freq[e] = 0;
        freq[e]++;
        if (!max_e || freq[e] > freq[max_e])
            max_e = e;
    }
    return max_e;
}

function mousePressed() {
    if (0 <= mouseX && mouseX < sz && 0 <= mouseY && mouseY < sz) {
        let distances = Array.from(points, p => [(p[0] - mouseX) ** 2 + (p[1] - mouseY) ** 2, p[2]]);
        distances.sort((a, b) => a[0] - b[0]);
        let voisins = Array.from(distances, p => p[1]);
        let k = input_k.value();
        if (k > 0 && k <= voisins.length) {
            let c = most_frequent(voisins.slice(0, k));
            points.push([mouseX, mouseY, c]);
            circle_nn = [mouseX, mouseY, 2 * distances[k - 1][0] ** 0.5];
        }
    }
}
