## Sample Test succeed!
import open3d as o3d

mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh.compute_vertex_normals()

o3d.visualization.draw_geometries([mesh])
## 안정화 문제로 현재는 사용하지 말 것
# o3d.visualization.draw(mesh, raw_mode=True)
