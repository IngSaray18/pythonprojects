from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl


# Deshabilitar verificación de certificados SSL (no recomendado en producción)
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE

# Conectarse a vCenter
si = SmartConnect(host='192.168.2.180', user='vspheregr.local\psaray', pwd='Vmware1!ps2023', sslContext=context)

# Obtener el objeto de servicio de inventario
content = si.RetrieveContent()

# Obtener todas las máquinas virtuales
vm_list = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
archivo = open('log.txt', 'a')    
# Procesar y mostrar información de las máquinas virtuales
for vm in vm_list.view:
    print(vm.name)
    print(f"Dirección IP: {vm.guest.ipAddress}")
    print(vm.guest.guestFullName)
    print(f"CPU: {vm.config.hardware.numCPU} vCPUs")
    print(f"Memoria: {vm.config.hardware.memoryMB} MB")
    print(f"Sistema operativo invitado: {vm.config.guestFullName}")
    print("-----")
    
    contenido_nuevo ="\n"+ vm.name + "\n" + vm.guest.ipAddress + "\n" + vm.guest.guestFullName + "\n -----"
    archivo.write(contenido_nuevo)

# Desconectar
# 
archivo.close()

Disconnect(si)
