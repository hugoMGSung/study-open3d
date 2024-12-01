# study-open3d
Open3D 따라하기

## 개요

### 참조
- 공식 사이트 - https://www.open3d.org/
- 깃헙 - https://github.com/isl-org/Open3D

## 튜토리얼

### 설치

```shell
pip install open3d
```

### 시각화 문제
- o3d.visualization.draw() 메서드 문제
    - Open3D 0.17.0 이상에 도입된 API 이나 일부 환경에서는 안정적이 못해 커널이 종료됨
    - 기존의 o3d.visualization.draw_geometries() 를 사용해야 함
    - raw_mode=True 옵션은 draw_geometries() 에서 동작하지 않음

### GPU 지원문제
- 기본은 CPU 버전으로 CUDA 버전을 설치하려면 아래 pip 설치

```shell
pip install open3d-gpu --extra-index-url https://pypi.nvidia.com 
```

### 테스트

https://github.com/user-attachments/assets/21b39f1a-fbf3-4072-b48d-a99bd22cd104

