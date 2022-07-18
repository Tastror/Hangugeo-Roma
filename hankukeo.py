import json
import pathlib
from functools import reduce

hankukeo_dict = {}

caeum = (
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
)
moeum = (
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
    "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ",
    "ㅣ"
)
patchim = (
    "　", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ",
    "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
)


def divide(single_korean) -> dict:
    global hankukeo_dict
    if hankukeo_dict is not None:
        with open("hankukeo.json", 'r') as hankukeo:
            hankukeo_dict = json.load(hankukeo)
    value = ord(single_korean)
    part_1 = (value - 44032) // 588
    part_2 = (value - 44032 - part_1 * 588) // 28
    part_3 = (value - 44032) % 28
    return {
        "org": single_korean,
        "res_str": caeum[part_1] + " " + moeum[part_2] + " " + patchim[part_3],
        "res": [caeum[part_1], moeum[part_2], patchim[part_3]],
        "value": [part_1, part_2, part_3],
    }


def roma(korean) -> dict:
    global hankukeo_dict
    if hankukeo_dict is not None:
        with open("hankukeo.json", 'r') as hankukeo:
            hankukeo_dict = json.load(hankukeo)
    res = []
    for mem in korean:
        if 44032 <= ord(mem) <= 55215:
            single_res = divide(mem)["res"]
            res.append(
                ("" if hankukeo_dict[single_res[0]] == "ng" else hankukeo_dict[single_res[0]])
                + hankukeo_dict[single_res[1]] + hankukeo_dict[single_res[2]]
            )
        elif (mem in caeum or mem in moeum or mem in patchim) and mem != "　":
            res.append(hankukeo_dict[mem])
        else:
            res.append(mem)
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
            output_korean = roma(input_korean)["res_str"]
        with (demo / (str(mem.stem) + "_out.txt")).open("w+", encoding="utf-8") as f:
            f.write(output_korean)

    # input_korean = "이것은 무엇 입니까?"
    # print(json.dumps(roma(input_korean), indent=4))
