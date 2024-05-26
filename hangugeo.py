import json
import pathlib
from functools import reduce

hangugeo_dict = {}

start = (
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
)
mid = (
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
    "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ",
    "ㅣ"
)
end = (
    " ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ",
    "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
)


def divide(single_korean) -> dict:
    global hangugeo_dict
    if hangugeo_dict is not None:
        with open("hangugeo.json", 'r') as hangugeo:
            hangugeo_dict = json.load(hangugeo)
    value = ord(single_korean)
    part_1 = (value - 44032) // 588
    part_2 = (value - 44032 - part_1 * 588) // 28
    part_3 = (value - 44032) % 28
    return {
        "org": single_korean,
        "res_str": start[part_1] + " " + mid[part_2] + " " + end[part_3],
        "res": [start[part_1], mid[part_2], end[part_3]],
        "value": [part_1, part_2, part_3],
    }


def roma(korean, use_separate) -> dict:
    global hangugeo_dict
    if hangugeo_dict is not None:
        with open("hangugeo.json", 'r') as hangugeo:
            hangugeo_dict = json.load(hangugeo)
    res = []
    last, now = False, False
    for mem in korean:
        if 44032 <= ord(mem) <= 55215:
            single_res = divide(mem)["res"]
            res.append(
                hangugeo_dict["start"][single_res[0]] +
                hangugeo_dict["mid"][single_res[1]] +
                hangugeo_dict["end"][single_res[2]]
            )
            now = True
        elif mem in start and mem != "ㅇ":
            res.append(hangugeo_dict["start"][mem])
            now = True
        elif mem in mid:
            res.append(hangugeo_dict["mid"][mem])
            now = True
        elif mem in end and mem != " ":
            res.append(hangugeo_dict["end"][mem])
            now = True
        else:
            res.append(mem)
            now = False
        if use_separate and last and now:
            res.insert(-1, "'")
        last = now
    return {
        "res_str": reduce(lambda x, y: x + y, res, ""),
        "res": res,
    }


if __name__ == "__main__":
    demo = pathlib.Path('demo')
    files = demo.glob("*.txt")
    deal_files = []
    for mem in files:
        if not str(mem).endswith("_out.txt"):
            deal_files.append(mem)
    for mem in deal_files:
        with mem.open("r", encoding="utf-8") as f:
            input_korean = f.read()
            output_korean = roma(input_korean, True)["res_str"]
        with (demo / (str(mem.stem) + "_out.txt")).open("w+", encoding="utf-8") as f:
            f.write(output_korean)

    input_korean = "이것은 무엇 입니까?"
    print(json.dumps(roma(input_korean, True), indent=4))
