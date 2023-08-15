from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# Deshabilitar verificación de certificado SSL (solo para propósitos de ejemplo)
ssl._create_default_https_context = ssl._create_unverified_context

# Parámetros de conexión
host = "TU_HOST"
user = "TU_USUARIO"
password = "TU_CONTRASEÑA"

# Conectarse al servidor vCenter
try:
    si = SmartConnect(host=host, user=user, pwd=password, port=443)
    content = si.RetrieveContent()

    # Obtener el objeto del clúster o datacenter donde se creará la VM
    cluster = None  # Debes configurar esto según tu entorno
    datacenter = cluster.parent

    # Definir la especificación de la VM
    vm_name = "MiNuevaVM"
    vm_folder = datacenter.vmFolder
    resource_pool = cluster.resourcePool
    datastore = None  # Debes configurar esto según tu entorno

    # Crear la especificación de la VM
    vmx_file = vim.vm.FileInfo(logDirectory=None, snapshotDirectory=None, suspendDirectory=None, vmPathName=None)
    config = vim.vm.ConfigSpec(name=vm_name, memoryMB=1024, numCPUs=1, files=vmx_file, guestId="ubuntu64Guest")

    # Crear la VM
    task = vm_folder.CreateVM_Task(config=config, pool=resource_pool, datastore=datastore)

    # Esperar a que la tarea se complete
    while task.info.state == vim.TaskInfo.State.running:
        continue

    # Imprimir el resultado de la tarea
    if task.info.state == vim.TaskInfo.State.success:
        print("Máquina virtual creada exitosamente.")
    else:
        print("Error al crear la máquina virtual:", task.info.error)

except Exception as e:
    print("Error de conexión:", e)

# Desconectar del servidor vCenter
Disconnect(si)
