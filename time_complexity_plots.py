import math
import plotly.graph_objects as go


def unk_fn_1(N):
    sum = 0
    i = 1
    while i < N:  # log(N) growth
        for j in range(0, N):  # N growth, log(N) times
            sum += 1
        i = i * 2
    return sum


def unk_fn_2(N):
    sum = 0
    n = N
    while n > 0:  # log(N) growth
        for i in range(0, n):  # log(N) growth, log(N) times
            sum += 1
        n = n // 2
    return sum


def log_time(N):
    sum = 0
    while N > 0:
        sum += 1
        N = N // 2
    return sum


def linear_time(N):
    sum = 0
    for i in range(N):
        sum += 1
    return sum


def linearithmic_time(N):
    sum = 0
    a = N
    while a > 0:
        b = a
        while b > 0:
            sum += 1
            b = b // 2
        a -= 1
    return sum


def quadratic_time(N):
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += 1
    return sum


results = []
for i in range(500):
    x = i

    unk1 = unk_fn_1(i)
    unk2 = unk_fn_2(i)

    log = log_time(i)
    linear = linear_time(i)
    linearithmic = linearithmic_time(i)
    quadratic = quadratic_time(i)

    results.append((x, unk1, unk2, log, linear, linearithmic, quadratic))

x = [i[0] for i in results]
unk1 = [i[1] for i in results]
unk2 = [i[2] for i in results]
log = [i[3] for i in results]
linear = [i[4] for i in results]
linearithmic = [i[5] for i in results]
quadratic = [i[6] for i in results]

fig = go.Figure(
    go.Scatter(x=x, y=unk1, mode='lines', name="O(UNK 1)", line=dict(color="red")),
)

fig.add_trace(
    go.Scatter(x=x, y=unk2, mode='lines', name="O(UNK 2)", line=dict(color="pink")),
)

fig.add_trace(
    go.Scatter(x=x, y=log, mode='lines', name="O(log(n))", line=dict(color="green")),
)

fig.add_trace(
    go.Scatter(x=x, y=linear, mode='lines', name="O(n)", line=dict(color="yellow")),
)

fig.add_trace(
    go.Scatter(x=x, y=linearithmic, mode='lines', name="O(n*log(n))", line=dict(color="blue")),
)

fig.add_trace(
    go.Scatter(x=x, y=quadratic, mode='lines', name="O(n^2)", line=dict(color="orange")),
)

# fig.update_xaxes(type="log")
# fig.update_layout(xaxis_type="log", yaxis_type="log")
# fig.update_xaxes(type="log", dtick=0.30102999566)

# fig.update_traces(textposition='top center')

fig.update_xaxes(
    scaleanchor="x",
    scaleratio=2,
)
fig.update_yaxes(
    range=(0, 500),
    constrain='domain'
)

fig.show()

for i in range(1, 50):
    print(i, i ** 2, math.log(i, 2), i * math.log(i, 2), math.log(i, 2) * math.log(i, 2))

for i in range(10000):
    print(f"i: {i}, fn: {unk_fn_2(i)}")

print("n, n^2, log(n), n*log(n) log^2(n)")


