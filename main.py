import os

def analyze_jeonse_contract(file_path):
    print(f"1. Document Parse: {file_path} 읽기 시작...")
    # (Upstage API 호출 로직)
    extracted_text = "임대인은 잔금 지급일 다음 날까지 담보권을 설정할 수 있다." 
    
    print("2. Solar LLM: 리스크 분석 중...")
    # Solar LLM에게 전달할 프롬프트(지시서)
    system_prompt = "너는 부동산 전문가야. 추출된 특약사항 또는 계약사항이 세입자에게 위험하면 경고해줘."
    
    # 가상의 분석 결과 (PoC용)
    result = {
        "risk_level": "High",
        "reason": "잔금일 다음 날 담보권 설정은 대항력 발생 전 대출을 허용하여 보증금 순위가 밀릴 위험이 큼.",
        "solution": "'잔금 지급일 익일까지 현재의 등기부 상태를 유지한다'로 수정 요청하세요."
    }
    return result

# 예시
if __name__ == "__main__":
    report = analyze_jeonse_contract("contract_sample.pdf")
    print(f"\n[진단 결과]\n위험도: {report['risk_level']}\n사유: {report['reason']}\n대응: {report['solution']}")
