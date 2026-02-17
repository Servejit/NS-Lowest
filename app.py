import gradio as gr

# -------- FUNCTION ----------
def parse_text(text):
    result = {}
    for line in text.splitlines():
        if ".NS" in line:
            parts = line.replace('"','').replace(',',' ').split()
            symbol = parts[0].replace(".NS","")
            prices = [float(x) for x in parts[1:] if "." in x]
            if prices:
                result[symbol] = min(prices)
    return result


# -------- COMPARE ----------
def compare(case1, case2):

    d1 = parse_text(case1)
    d2 = parse_text(case2)

    output = "{\n"

    for s in d1:
        price = min(d1[s], d2.get(s, d1[s]))
        output += f'"{s}.NS": {price:.2f},\n'

    output += "}"

    return output


# -------- CONVERT ----------
def convert(case3):

    result = []

    for line in case3.splitlines():
        if ".NS" in line:
            result.append(f'"{line.split(chr(34))[1]}"')

    return ", ".join(result)


# -------- UI ----------
with gr.TabbedInterface(

    [

        gr.Interface(
            fn=compare,
            inputs=[
                gr.Textbox(lines=15, label="Case 1"),
                gr.Textbox(lines=15, label="Case 2")
            ],
            outputs="text",
            title="Compare"
        ),

        gr.Interface(
            fn=convert,
            inputs=gr.Textbox(lines=15, label="Case 3"),
            outputs="text",
            title="Convert"
        )

    ],

    ["Compare", "Convert"]

) as app:

    pass


app.launch()
