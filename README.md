"# Brats" 

## 1. Service inform

![image.png](img/sv1.png)

- 뇌 종양의 위치 및 Size를 예측하여 해당 부위에 이상이 생겼을 경우, 나타나는 증상을 알려줌
- 과거 기록을 바탕으로 소견서 생성해줌
- 두 가지 기능을 종합, web으로 구현하여 Service를 제공

## 2. Service Pipeline

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03045eb3-ad52-466e-993e-65791c3db2bf/67eb3676-c345-40e6-af33-2d657b61310f/image.png)

- Segmentation : 종양의 3D img & 위치 및 Size 출력
- Rag : Segmentation 에서 위치 및 Size data를 받아 Neurology PDF에서 찾음 → 증상출력
- LLM : 과거 진단기록 요약하여 소견서 생성

## 3. Service output

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03045eb3-ad52-466e-993e-65791c3db2bf/b26fb9a2-4e17-4903-9d50-96032bf073e2/image.png)

## 4. 기술별 workflow

[3D Segmentation](https://www.notion.so/3D-Segmentation-162c4cba74ea809184d7d40e0fd3ff51?pvs=21)

[Rag](https://www.notion.so/Rag-162c4cba74ea809aa02bfc3cc8d7069e?pvs=21)

[LLM](https://www.notion.so/LLM-162c4cba74ea80488745d9b4d9eab264?pvs=21)

## 5. Tech & Member

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03045eb3-ad52-466e-993e-65791c3db2bf/ebb5ec44-f02d-44c8-9b5a-8a7d26d26727/image.png)

## Time line

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03045eb3-ad52-466e-993e-65791c3db2bf/0c6fffbd-f475-47ec-b2ed-0962a902af43/image.png)
